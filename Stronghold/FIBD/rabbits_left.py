import sys

# Each pair reaches maturity in 1 month
# Upon maturity, 2 rabbits produced
# Pairs die after m months

def final_rabbit_count(n, m):
    rabbits = [1, 1]
    for i in range(n):
        curr = rabbits[-1]
        if len(rabbits) > m - 1:
            curr -= rabbits[-m]
        curr += rabbits[-2]
        rabbits.append(curr)
    return rabbits[-1]

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
