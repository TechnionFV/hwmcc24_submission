#!/usr/bin/env python

import sys
import os
import os.path
import atexit
import tempfile
import shutil
import subprocess as sub
import threading
import signal
import time
import resource
import itertools

import aig
#
# globals ...
#
root = os.path.dirname (os.path.realpath (__file__))
verbose = True      # TODO: make an option
running = list()    # list of running processes

###############################################################################


class SolverCfg (object):
    def __init__ (self, name, cmd, cpu=-1, mem=-1):
        self._name = name
        self._cmd = cmd
        self._cpu = cpu
        self._mem = mem
        
    @property
    def name (self): return self._name
    @property 
    def cmd (self): return self._cmd
    @property
    def cpu (self): return self._cpu
    @property
    def mem (self): return self._mem
    
    def append_arg (self, arg): self._cmd.append (arg)
    
    def __str__ (self):
        return '[' + self.name + '] ' + ' '.join (self.cmd)


def profiles ():
    
    profs = dict ()    
    def reg_profile (cfg): profs [cfg.name] = cfg

    reg_profile (SolverCfg ('avymin', 
                            [getAvy (), '--reset-cover=1', '-a',
                             '--kstep=1',
                             '--shallow-push=1', '--tr0=1', '--min-suffix=1', 
                             '--glucose', '--glucose-inc-mode=1',
                             '--sat-simp=0', '--minisat_itp=1']))
    reg_profile (SolverCfg ('avysimp', 
                            [getAvy (), '--reset-cover=1', '-a',
                             '--kstep=1',
                             '--shallow-push=1', '--tr0=1', '--min-suffix=0', 
                            '--glucose', '--glucose-inc-mode=1',
                             '--sat-simp=1', '--minisat_itp=1']))
    reg_profile (SolverCfg ('avylong', 
                            [getAvy (), '--reset-cover=1', '-a',
                             '--kstep=2', '--stick-error=1',
                             '--shallow-push=1', '--tr0=1', '--min-suffix=1', 
                             '--glucose', '--glucose-inc-mode=1',
                             '--sat-simp=1', '--minisat_itp=1']))
    reg_profile (SolverCfg ('avylonglong', 
                            [getAvy (), '--reset-cover=1', '-a',
                             '--kstep=4', '--stick-error=1',
                             '--shallow-push=1', '--tr0=1', '--min-suffix=1', 
                             '--glucose', '--glucose-inc-mode=1',
                             '--sat-simp=1', '--minisat_itp=1']))
    reg_profile (SolverCfg ('abcpdr', [getAbcPdr()]))
    reg_profile (SolverCfg ('avymus', 
                            [getAvy (), '--reset-cover=1',
                             '--kstep=1',
                             '--shallow-push=1', '--tr0=1', '--min-suffix=0', 
                             '--glucose', '--glucose-inc-mode=1', '--min-core=1',
                             '--minisat_itp=1']))
    reg_profile (SolverCfg ('avyabsmus', 
                            [getAvy (), '--reset-cover=1', '-a',
                             '--kstep=1',
                             '--shallow-push=1', '--tr0=1', '--min-suffix=0', 
                             '--glucose', '--glucose-inc-mode=1', '--min-core=1',
                             '--minisat_itp=1']))                  
    return profs

def list_profiles (option, opt_str, value, parser):
    for p in profiles ().itervalues (): print str(p)
    sys.exit (0)

def parseOpt (argv):
    from optparse import OptionParser
    
    parser = OptionParser ()
    parser.add_option ('--list-profiles', action="callback",
                       callback=list_profiles,
                       help='List all available profiles')
    parser.add_option ('-p', '--profiles', type=str, 
                       default='avymin:avysimp:avylong:avylonglong:abcpdr:avymus:avyabsmus')
    parser.add_option ("--save-temps", dest="save_temps",
                       help="Do not delete temporary files",
                       action="store_true",
                       default=False)
    parser.add_option ("--temp-dir", dest="temp_dir",
                       help="Temporary directory",
                       default=None)
    parser.add_option ('--pp-cpu', dest='pp_cpu',
                       help='CPU time limit (seconds) for pre-processing',
                       type=int, default=120)
    parser.add_option ('--cex', type=str, default='-')
    # parser.add_option ('--cpu', type='int', dest='cpu',
    #                    help='CPU time limit (seconds) TEMP: has no effect', 
    #                    default=-1)
    # parser.add_option ('--mem', type='int', dest='mem',
    #                    help='MEM limit (MB) TEMP: has no effect', default=-1)

    (options, args) = parser.parse_args (argv)

    return (options, args)

def createWorkDir (dname = None, save = False):    
    if dname == None:
        workdir = tempfile.mkdtemp (prefix='avy-')
    else:
        workdir = dname
    if verbose: print "Working directory", workdir
    if not save: atexit.register (shutil.rmtree, path=workdir)
    return workdir

def getPyPath(script):
    fn = os.path.join (root, script)
    if not isexec (fn): raise IOError ("Cannot find " + script)
    return fn

def isexec (fpath):
    if fpath == None: return False
    return os.path.isfile(fpath) and os.access(fpath, os.X_OK) 

def cat (in_file, out_file): out_file.write (in_file.read ())

def which(program):
    fpath, fname = os.path.split(program)
    if fpath:
        if isexec (program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if isexec (exe_file):
                return exe_file
    return None

def runPP (workdir, in_name, cpu=-1):     
    '''pre-processing '''
    if verbose: print "[pavy] in_name = ", in_name

    out_name = os.path.basename (in_name)
    out_name, ext = os.path.splitext (out_name)
    out_name = os.path.join (workdir, out_name + '.pp' + ext)
    
    abc_args = [getAbc (),
                '-c',
                '&r {x} ; &lcorr ; &scorr; &fraig ; &w {y}'.format (x=in_name,
                                                                    y=out_name)]
    if verbose: print '[pavy]', ' '.join (abc_args)


    def _set_limits ():
        if cpu > 0:
            resource.setrlimit (resource.RLIMIT_CPU, [cpu, cpu])
   
    try:
        sub.check_call (abc_args, preexec_fn=_set_limits)
    except sub.CalledProcessError as e:
        if verbose:
            print '[pavy] pre-processing failed with', e

        abc_args = [getAbc (), '-c', 
                    '&r {x} ; &w {y}'.format(x=in_name,y=out_name)]
        try:
            if verbose: print '[pavy] trivial pre-processing'
            sub.check_call (abc_args)
        except sub.CalledProcessError as e2:
            if verbose: print '[pavy] trivial pre-processing failed with', e2
            out_name = in_name
    return out_name
    
def runProc (args, fname, stdout, stderr, cpu=-1, mem=-1):
    '''Kicks off a specified exec (args) on input fname, with specified 
    stdout/stderr
    ''' 
    args += [fname]
    if verbose: 
        print "[pavy] kicking off ", ' '.join (args)
        
    def _set_limits ():
        if mem > 0:
            mem_b = mem * 1024 * 1024
            resource.setrlimit (resource.RLIMIT_AS, [mem_bytes, mem_bytes])
        if cpu > 0:
            resource.setrlimit (resource.RLIMIT_CPU, [cpu, cpu])

    return sub.Popen (args,
                      stdout=open (stdout, 'w'),
                      stderr=open (stderr, 'w'),
                      preexec_fn=_set_limits)
    
def getAvy ():
    avy = which ("avy")
    if avy is None: 
        raise IOError ("Cannot find avy")
    return avy
def getAbc ():
    abc = which ('abc')
    if abc is None:
        raise IOError ('Cannot find abc')
    return abc
def getAbcPdr ():
    f = which ('abcpdr')
    if f is None:
        raise IOError ('Cannot find abcpdr')
    return f

def run (workdir, fname, profs, cex_name='-', pp_cpu=-1, cpu=-1, mem=-1):
    '''Run everything and wait for an answer'''

    if len (profs) == 0: return

    def of (n):
        if n == '-': return sys.stdout
        else: return open (n, 'wb')

    print "[pavy] starting run with fname={f}".format(f=fname)
    
    print "BRUNCH_STAT Result UNKNOWN"
    sys.stdout.flush ()

    print "[pavy] running pp" 
    pp_name = runPP (workdir, fname, cpu=pp_cpu)
    print "[pavy] finished pp, output={f}".format(f=pp_name)

    ## names of configurations
    p = profiles ()
    cfgs = [p[x] for x in profs]
    if verbose: 
        for c in cfgs: c.append_arg ('--verbose=2')

    name = os.path.splitext (os.path.basename (pp_name))[0]
    stdout = [os.path.join (workdir, cfgs[i].name + '_avy{0}.stdout'.format (i)) 
              for i in range(len (cfgs))]
    stderr = [os.path.join (workdir, cfgs[i].name + '_avy{0}.stderr'.format (i))
              for i in range (len (cfgs))]
    cex = [os.path.join (workdir, cfgs[i].name + '_avy{0}.cex'.format (i)) 
              for i in range(len (cfgs))]
    
    for i, c in zip (itertools.count(), cfgs): 
       c.append_arg ('--cex={0}'.format (cex [i]))
    
    global running
    running.extend ([runProc (cfgs [i].cmd, pp_name, stdout[i], stderr [i], 
                              cpu=cfgs[i].cpu, mem=cfgs[i].mem)
                     for i in range (len (cfgs))])

    orig_pids = [p.pid for p in running]
    pids = [p.pid for p in running ]
    pid = -1
    exit_code = 2
    sig = -1
    returnvalue = -1
    while len (pids) != 0:
        print "[pavy] running: %r" % pids

        try:
            (pid, returnvalue, ru_child) = os.wait4 (-1, 0)
        except OSError:  # probably got interrupted
            break
        (exit_code, sig) = (returnvalue // 256, returnvalue % 256) 

        print "[pavy] finished pid %d with code %d and signal %d" % \
            (pid, exit_code, sig)

        pids.remove (pid)
        
        
        # exit codes: 0 = UNSAFE, 1 = SAFE, 2 = UNKNOWN, 3 = validation error
        if sig == 0 and (exit_code == 0 or exit_code == 1):
            for p in pids:
                try:
                    print "[pavy] trying to kill ", p
                    #os.killpg (p, signal.SIGTERM)
                    os.kill(p, signal.SIGTERM)
                except OSError: pass
                finally:
                    try:
                        print "[pavy] waiting for ", p         
                        os.waitpid (p, 0)
                    except OSError: pass
            break
    
    if sig == 0 and (exit_code == 0 or exit_code == 1):
        idx = orig_pids.index (pid)
        cat (open (stdout [idx]), sys.stdout)
        cat (open (stderr [idx]), sys.stderr)
        if verbose: print '[pavy] Witness begin'
        if exit_code == 1:
            aig.adjust_cex (in_cex=open (cex [idx]),
                            cex_aig=aig.parse (open (pp_name)),
                            orig_aig=aig.parse (open (fname)),
                            out_cex=of(cex_name))
        elif exit_code == 0:
            # print the unsat witness
            print '0\nb0\n.'
            
        if verbose: print '[pavy] Witness end'    
            
        print 'WINNER: ', cfgs[idx].name
        print 'BRUNCH_STAT config {0}'.format (idx)
        print 'BRUNCH_STAT config_name {0}'.format (cfgs [idx].name)
        print 'BRUNCH_STAT Result ' + ('UNSAT' if exit_code == 0 else 'SAT')
    else:  
        if verbose:
            for idx, std, err in zip (itertools.count (), stdout, stderr):
                print >> sys.stdout, '[pavy] LOG BEGIN', cfgs[idx].name 
                cat (open (std), sys.stdout)
                print >> sys.stdout, '[pavy] LOG END', cfgs[idx].name 
                print >> sys.stderr, '[pavy] LOG BEGIN', cfgs[idx].name 
                cat (open (err), sys.stderr)
                print >> sys.stderr, '[pavy] LOG END', cfgs[idx].name 
                
        print "ALL INSTANCES FAILED"
        print 'Calling sys.exit with {0}'.format (returnvalue // 256)
        print 'BRUNCH_STAT config -1'
        print 'BRUNCH_STAT config_name None'
        print 'BRUNCH_STAT Result UNKNOWN'
        sys.exit (returnvalue // 256)

    running[:] = []
    return exit_code

def main (argv):
    os.setpgrp ()

    (opt, args) = parseOpt (argv[1:])

    workdir = createWorkDir (opt.temp_dir, opt.save_temps)
    returnvalue = 0
    for fname in args:
        returnvalue = run(workdir, fname=fname, profs=opt.profiles.split (':'), 
                          cex_name = opt.cex, pp_cpu=opt.pp_cpu)
    return returnvalue

def killall ():
    global running
    for p in running:
        try:
            if p.poll () == None:
                p.terminate ()
                p.kill ()
                p.wait ()
                # no need to kill pg since it kills its children
        except OSError:   pass
    running[:] = []

if __name__ == '__main__':
    # unbuffered output
    sys.stdout = os.fdopen (sys.stdout.fileno (), 'w', 0)
    os.environ['PATH'] = '.' + os.pathsep + os.environ ['PATH']

    try:
        signal.signal (signal.SIGTERM, lambda x, y: killall())
        sys.exit (main (sys.argv))
    except KeyboardInterrupt: pass
    finally: killall ()
            
