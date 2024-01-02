import os
import sys
import uuid

def main():
    args = sys.argv[1:]

    filename = "/tmp/tempfile-" + uuid.uuid4().hex

    with open(filename, "w") as f:
        f.write(" ".join(args))

    print(filename)

if __name__ == "__main__":
    main()
