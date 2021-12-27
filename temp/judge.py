import argparse
import glob
import subprocess


def run_command(cmd):
    result = subprocess.run(cmd, shell=True)
    return result


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("problem_id", type=str, help="問題のID, 例: a, A")
    parser.add_argument("-s",
                        "--submit",
                        action="store_true",
                        help="'-s' をつけると、サンプルが全て通っていた時に自動で提出する")
    parser.add_argument("-e",
                        "--error",
                        type=float,
                        default=0,
                        help="許容誤差, 例: 1e-6, 0.1")
    parser.add_argument("-p",
                        "--python",
                        action="store_true",
                        help="'-p' をつけると、Pythonで提出する（付けない場合はPyPy）")

    args = parser.parse_args()
    return args


def judge(problem_id, allowable_error):
    tests_folder_path = glob.glob(f"**/{problem_id}/tests")[0]

    if allowable_error:
        judge_cmd = f"oj t -e {allowable_error} -c 'python3 {problem_id}.py' -d {tests_folder_path}"
    else:
        judge_cmd = f"oj t -c 'python3 {problem_id}.py' -d {tests_folder_path}"

    result = run_command(judge_cmd)
    pass_all_sample_cases = result.returncode == 0
    return pass_all_sample_cases


def submit(problem_id, submit_by_python):
    if submit_by_python:
        submit_cmd = f"python3 submit.py {problem_id} -l python"
    else:
        submit_cmd = f"python3 submit.py {problem_id} -l pypy"

    run_command(submit_cmd)
    return


def main():
    args = parse_arguments()
    problem_id = args.problem_id.lower()
    submit_code = args.submit
    allowable_error = args.error
    submit_by_python = args.python

    pass_all_sample_cases = judge(problem_id, allowable_error)

    if pass_all_sample_cases and submit_code:
        submit(problem_id, submit_by_python)
    return


if __name__ == "__main__":
    main()
