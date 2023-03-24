import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python transcribe [TXT file]")
        return 1
    f = open(sys.argv[1], "r").read()
    print(f.replace("T", "U"))
    return 0

if __name__ == "__main__":
    main()
