import sys

# 5 Months
# 1st Month, 1 Rabbit Pair
# 2nd Month, 1 Rabbit Pair
# 3rd Month, 4 Rabbit Pair
# 4th Month, 7 Rabbit Pair
# 5th Month, 19 Rabbit Pair

def final_rabbit_count(n, k):
    rabbits = [1, 1, 1 + k]
    for i in range(n - 3):
        rabbits.append(rabbits[-1] + rabbits[-2] * k)
    return rabbits[-1]

def main():
    if len(sys.argv) != 2:
        print("Usage: python rabbit_count.py [TXT file]")
        return 1
    f = open(sys.argv[1], "r").read()
    [n, k] = f.split()
    print(final_rabbit_count(int(n), int(k)))
    return 0

if __name__ == "__main__":
    main()
