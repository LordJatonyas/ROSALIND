import sys

def rev_com(s):
    res = ""
    complements = {"A": "T", "T": "A", "C": "G", "G": "C"}
    for i in range(len(s) - 1, -1, -1):
        if s[i] in complements:
            res += complements[s[i]]
    return res

def main():
    if len(sys.argv) != 2:
        print("Usage: python rev_complement.py [TXT file]")
        return 1
    f = open(sys.argv[1], "r").read()
    print(rev_com(f))
    return 0

if __name__ == "__main__":
    main()
