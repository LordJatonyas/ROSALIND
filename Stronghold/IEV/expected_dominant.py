import sys

def expected_value(couples):
    res = 0
    res += 1 * (int(couples[0]) + int(couples[1]) + int(couples[2]))
    res += 0.75 * int(couples[3])
    res += 0.5 * int(couples[4])
    return res

def main():
    if len(sys.argv) != 2:
        print("Usage: python graph.py [TXT file]")
        return 1
    f = open(sys.argv[1], "r").read()
    couples = f.split()
    expected_offsprings_count = 2 * expected_value(couples)
    print(expected_offsprings_count)
    return 0

if __name__ == "__main__":
    main()
