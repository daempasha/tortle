import sys


def main():
    # Implement REPL (https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)
    while True:
        # Wait for user input
        sys.stdout.write("$ ")
        command = input()
        
        # Echo
        if command.startswith("echo "):
            print(command[5:])
            continue

        # Exit
        if command == "exit 0":
            exit(0)
        print(f"{command}: command not found")
        
    

if __name__ == "__main__":
    main()
