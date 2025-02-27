import sys
import os
import shutil

def main():
    # Implement REPL (https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)
    while True:
        # Wait for user input
        sys.stdout.write("$ ")
        command = input()
        
        implemented_commands = ["type", "echo", "exit"]
        path = os.environ["PATH"]
        # Type
        if command.startswith("type "):
            command_name = command[5:]
            # Check if command in path
            if command_name in implemented_commands:
                print(f"{command_name} is a shell builtin")
            elif path := shutil.which(command_name): # basically path = shutil.which(command_name); if path:
                print(f"{command_name} is {path}")
            else:
                print(f"{command_name}: not found")
            continue

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
