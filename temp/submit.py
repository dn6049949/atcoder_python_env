import argparse
import glob
import json
import subprocess


def run_command(cmd):
    result = subprocess.run(cmd, shell=True)
    return result


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("problem_id", type=str, help="問題のID, 例: a, A")
    parser.add_argument("-l",
                        "--language",
                        type=str,
                        default="pypy",
                        help="提出言語, デフォルト: pypy, 対応しているのはpypyとpythonのみ")

    args = parser.parse_args()
    return args


def submit(problem_id, language_code):
    task_url = extract_task_url(problem_id)

    submit_cmd = f"oj s -l {language_code} -y --no-open {task_url} {problem_id}.py"

    run_command(submit_cmd)
    return


def extract_task_url(problem_id):
    contest_info_path = glob.glob(f"**/contest.acc.json")[0]

    with open(contest_info_path, "r") as f:
        contest_info = json.load(f)

    tasks_info = contest_info["tasks"]
    for task_info in tasks_info:
        if task_info["label"].lower() == problem_id:
            task_url = task_info["url"]
            return task_url

    return None


def main():
    args = parse_arguments()
    problem_id = args.problem_id.lower()
    language = args.language.lower()

    language_codes = {"pypy": 4047, "python": 4006}

    language_code = language_codes[language]

    submit(problem_id, language_code)
    return


if __name__ == "__main__":
    main()
