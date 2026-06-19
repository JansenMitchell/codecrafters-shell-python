import sys


def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == "exit":
            sys.exit()
        elif command.startswith("echo"):
            string = command[5:]
            print(f"{string}")
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
