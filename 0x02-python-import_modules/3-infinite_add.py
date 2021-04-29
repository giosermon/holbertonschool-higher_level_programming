#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = 0
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            n += int(sys.argv[i])
    print(n)
