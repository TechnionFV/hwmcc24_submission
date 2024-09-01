import multiprocessing
import os
import subprocess
from multiprocessing import Pool

"""
***************************************************************************************************
list all files
***************************************************************************************************
"""


def __get_all_file_paths_in_dir_recursively(rootdir: str) -> list[str]:
    result = []
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            file_path = os.path.join(subdir, file)
            result += [file_path]
    return result


def __filter_list_of_string_by_ending(list_of_strings: list[str], desired_ending: str) -> list[str]:
    filtered = []
    for f in list_of_strings:
        if f[-len(desired_ending):] == desired_ending:
            filtered += [f]
    return filtered


def __get_all_file_paths_in_dir_that_have_desired_ending(rootdir: str, desired_ending):
    files_in_root = __get_all_file_paths_in_dir_recursively(
        rootdir=rootdir
    )
    filtered_inputs = __filter_list_of_string_by_ending(
        list_of_strings=files_in_root,
        desired_ending=desired_ending
    )
    return filtered_inputs


def list_all_aig_files(root: str) -> list[str]:
    return __get_all_file_paths_in_dir_that_have_desired_ending(
        rootdir=f"{root}/tests",
        desired_ending=".aig"
    )


"""
***************************************************************************************************
local test
***************************************************************************************************
"""

profiles = ['avymin', 'avysimp', 'navy', 'abcpdr', 'fib', 'kavy1', 'kavy2', 'kavy3', 'Macallan',
            'JohnnieWalker', 'Jameson', 'Glenlivet', 'RFVEV', 'RFV']


def __custom_run_cmd(i_cmd: tuple[int, str]):
    i, cmd = i_cmd
    print(f"--- i = {i} RUNNING {cmd}")
    proc = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    is_error = proc.returncode != 0
    is_error = is_error or "AssertionError" in proc.stderr
    is_error = is_error or "AssertionError" in proc.stdout
    if is_error:
        m = f"Error when running command {cmd}"
        print(m)
        print(f"STDOUT:\n{proc.stdout}")
        print(f"STDERR:\n{proc.stderr}")
        raise Exception(m)


def local_test():
    assert os.path.exists("../tests") and os.path.exists("../scripts/pavy.py")
    root = os.path.realpath("..")
    assert root.endswith("hwmcc24_submission")
    tests = list_all_aig_files(root=root)
    timeout_in_seconds = 10
    threads_to_use = 1 # multiprocessing.cpu_count()
    time_of_test_minutes = 5
    time_of_test_in_seconds = time_of_test_minutes * 60
    n = int((time_of_test_in_seconds / timeout_in_seconds) * threads_to_use)
    print(f"number of tests to run = {n}")
    commands = []

    for i, test in enumerate(tests):
        for profile in profiles:
            w = f"/tmp/{profile}_witnesses"
            if not os.path.exists(w):
                os.mkdir(w)
            command = f"python3 {root}/scripts/pavy.py --certificate={w}/cert_{i} --cex={w}/cex_{i} {test} --cpu {timeout_in_seconds} --check -p {profile}"
            commands += [command]

    os.environ['PATH'] = f'{root}/executables/' + os.pathsep + os.environ['PATH']
    os.system(f"export PATH={root}/executables/:$PATH")
    from random import shuffle
    shuffle(commands)
    commands = list(enumerate(commands))
    commands = commands[:n]
    with Pool(threads_to_use) as p:
        try:
            list(p.imap_unordered(__custom_run_cmd, commands))
        except Exception as e:
            print(f"a worker failed, aborting...\nError: {e}")
            p.close()
            p.terminate()
            raise e


"""
***************************************************************************************************
main
***************************************************************************************************
"""


def main():
    print("Test start")
    local_test()
    print("Test passed")


if __name__ == "__main__":
    main()
