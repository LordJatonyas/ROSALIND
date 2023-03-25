import sys

# The number of positions that two codewords of the same length
# differ is the Hamming distance. For DNAs, it's the number of 
# bases that are different between 2 DNA strings (in order).
def calculate(s1, s2):
    mismatches = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            mismatches += 1
    return mismatches

def main():
    if len(sys.argv) != 2:
        print("Usage: python hamming_distance.py [TXT file]")
        return 1
    f = open(sys.argv[1], "r").read().split("\n")
    print(calculate(f[0], f[1]))
    return 0

if __name__ == "__main__":
    main()
