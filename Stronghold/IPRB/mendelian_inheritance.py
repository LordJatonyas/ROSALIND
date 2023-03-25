import sys

def calculate(k, m, n):
    denom = (k + m + n - 1)/2 * (2 + (k + m + n - 2))
    num = denom - (m + n - 1)/2 * (2 + (m + n - 2))
    num += (m - 1)/2 * (2 + (m - 2)) * 0.75
    num += m * n * 0.5
    return num/denom

def main():
    if len(sys.argv) != 2:
        print("Usage: python mendelian_inheritance.py [TXT file]")
        return 1
    f = open(sys.argv[1], "r").read().split()
    print("{:.5f}".format(calculate(int(f[0]), int(f[1]), int(f[2]))))
    return 0

if __name__ == "__main__":
    main()
