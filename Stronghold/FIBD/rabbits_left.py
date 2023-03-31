import sys

def final_rabbit_count(n, m):
    rabbits = [(1,0), (0,1)]
    for _ in range(n - 2):
        # if no rabbits die
        if len(rabbits) < m:
            rabbits.append((rabbits[-1][1], rabbits[-1][0] + rabbits[-1][1]))
        # Gets weird when rabbits start dying...
        else:
            rabbits.append((rabbits[-1][1], rabbits[-1][0] + rabbits[-1][1] - rabbits[-m][0]))
    return rabbits[-1][0] + rabbits[-1][1]

def main():
    if len(sys.argv) != 2:
        print("Usage: python rabbit_count.py [TXT file]")
        return 1
    f = open(sys.argv[1], "r").read()
    [n, m] = f.split()
    print(final_rabbit_count(int(n), int(m)))
    return 0

if __name__ == "__main__":
    main()
