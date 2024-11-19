"""windows shell"""
from user_commands import command as cmd


def main():
    # 创建解析器 自己的shell解析器
    # parser = argparse.ArgumentParser(description="god-shell")
    # # parser.add_argument("command", help="command to run")
    # args = parser.parse_args('command')
    # print(args.command)
    print("Welcome to god_say!")
    while True:
        # 等待用户输入命令
        command = input("make a wish: ")
        # 把command去除“make a wish”部分，并用空格分割成列表
        args: list = command.split()
        if not cmd.Command.is_command(args[0]):
            print("Invalid command")
            continue
        else:
            cmd.Command.execute(args[0], args[1:])

            # 如果输入exit，则退出程序


if __name__ == "__main__":
    main()
