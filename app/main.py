import sys
import os
import shutil

def main():
    # Implement REPL (https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)
    while True:
        # Wait for user input
        sys.stdout.write("$ ")
        command = input()
        
        implemented_commands = ["type", "echo", "exit", "pwd"]
        path = os.environ["PATH"]
        # Type
        args = command.split(" ")
        
        if args[0] == "pwd":
            print(os.getcwd())
            continue

        if args[0] == "type":
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
        if args[0] == "echo":
            print(command[5:])
            continue

        # Exit
        if args[0] == "exit" and args[1] == "0": 
            exit(0)

        # Is executable
        if path := shutil.which(args[0]):
            os.system(command)
        else:
            print(f"{command}: command not found")
        
    

if __name__ == "__main__":
    main()
