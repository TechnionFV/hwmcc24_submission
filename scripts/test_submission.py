import multiprocessing
import os
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
    proc = os.system(cmd)
    assert False
    # print(proc.stderr)
    assert proc.returncode == 0
    assert "AssertionError" not in proc.stderr


def local_test():
    assert os.path.exists("../tests") and os.path.exists("../scripts/pavy.py")
    root = os.path.realpath("..")
    assert root.endswith("hwmcc24_submission")
    tests = list_all_aig_files(root=root)
    timeout_in_seconds = 10
    threads_to_use = multiprocessing.cpu_count()
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
    with Pool(threads_to_use) as p:
        p.map(__custom_run_cmd, commands)


"""
***************************************************************************************************
main
***************************************************************************************************
"""


def main():
    local_test()


if __name__ == "__main__":
    main()