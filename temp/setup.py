import argparse
import os
import subprocess


def parse_arguments():
    current_directory = os.getcwd()
    default_contest_id = os.path.basename(current_directory)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--contest_id",
        type=str,
        default=default_contest_id,
        help=
        "コンテストのID(コンテストトップページのURLの末尾), 例: abc100, arc100\n"
        "指定しない場合はカレントディレクトリの末尾をコンテストIDとする"
    )

    args = parser.parse_args()
    return args


def run_command(cmd):
    result = subprocess.run(cmd, shell=True)
    return result


def login_oj():
    oj_login_cmd = "oj login https://atcoder.jp/"
    run_command(oj_login_cmd)
    return


def build_acc_environment(contest_id):
    print(f"Build acc environment. contest ID: '{contest_id}'")

    apply_config_cmd = "acc config default-task-choice all"
    run_command(apply_config_cmd)

    acc_setting_cmd = f"acc new {contest_id}"
    run_command(acc_setting_cmd)
    return


def main():
    args = parse_arguments()
    contest_id = args.contest_id

    login_oj()
    build_acc_environment(contest_id)
    return


if __name__ == "__main__":
    main()
