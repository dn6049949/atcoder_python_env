import argparse
import os
import shutil


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("contest_dir_path",
                        type=str,
                        help="コンテスト環境を作成するディレクトリのパス")
    parser.add_argument("-p",
                        "--pass-add-tool",
                        action="store_true",
                        help="'-p' をつけると、judgeなどのツールを作成しない")
    parser.add_argument("-n",
                        "--number",
                        type=int,
                        default=8,
                        help="問題の数、デフォルトは8")

    args = parser.parse_args()
    return args


def confirm_to_build_environment(contest_dir_path):
    print(f"Directory '{contest_dir_path}' already exists.")
    choice = input(
        "Do you want to delete files and rebuild it? [y/N]: ").lower()

    if choice in ["y", "ye", "yes"]:
        return True

    else:
        return False


def add_tool_files(contest_dir_path):
    tools = ("judge", "submit", "setup")

    for tool in tools:
        template_tool_file_path = os.path.join("temp", f"{tool}.py")
        contest_tool_file_path = os.path.join(contest_dir_path, f"{tool}.py")
        shutil.copy(template_tool_file_path, contest_tool_file_path)

    return


def add_task_files(contest_dir_path, task_num):
    template_task_file_path = os.path.join("temp", "temp.py")

    for task_index in range(task_num):
        task_id = chr(ord("a") + task_index)
        task_file_path = os.path.join(contest_dir_path, f"{task_id}.py")
        shutil.copy(template_task_file_path, task_file_path)

    return


def main():
    args = parse_arguments()
    contest_dir_path = args.contest_dir_path
    pass_add_tool = args.pass_add_tool
    task_num = args.number

    if os.path.exists(contest_dir_path):
        if confirm_to_build_environment(contest_dir_path):
            print("Rebuild contest environment.")
            shutil.rmtree(contest_dir_path)

        else:
            print("Skip build.")
            exit(0)

    os.makedirs(contest_dir_path)

    add_task_files(contest_dir_path, task_num)

    if not pass_add_tool:
        add_tool_files(contest_dir_path)

    return


if __name__ == "__main__":
    main()
