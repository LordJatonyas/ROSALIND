import sys

def count_bases(s):
    bases = {"A": 0, "C": 0, "G": 0, "T": 0}
    for c in s:
        if c in bases:
            bases[c] += 1
    return bases["A"], bases["C"], bases["G"], bases["T"]

def main():
    if len(sys.argv) != 2:
        print("Usage: python count_bases.py [TXT file]")
        return 1
    f = open(sys.argv[1], "r").read()
    a,c,g,t = count_bases(f)
    print(f'{a} {c} {g} {t}')
    return 0

if __name__ == "__main__":
    main()
