import sys


def main():
    sys.stdout.write("$ ")
    command = sys.argv[1]
    if command:
        print(f"{command}: command not found")


if __name__ == "__main__":
    main()
