import os
import sys
import subprocess

def run(args):
    exit(subprocess.run(args).returncode)

def main():
    args = sys.argv[1:]

    if not args:
        run(["exa"])
        return

    for arg in args:
        if os.path.exists(arg):
            if os.path.isdir(arg):
                mode = "ls"
                break
            else:
                mode = "cat"
                break
    else:
        print("No files or folders in args")
        exit(1)

    if mode == "cat":
        run(["bat"] + args)
    else:
        run(["exa"] + args)

if __name__ == "__main__":
    main()
