import sys

def find_motifs(s, m):
    if len(m) > len(s):
        return [0]
    n = len(m)
    res = list()
    for i in range(len(s)):
        if i + n >= len(s):
            break
        if s[i:i+n] == m:
            res.append(i + 1)
    return res

def main():
    if len(sys.argv) != 2:
        print("Usage: python motif_indices.py [TXT file]")
        return 1
    f = open(sys.argv[1], "r").read().split('\n')
    strand, motif = f[0], f[1]
    print(" ".join(str(x) for x in find_motifs(strand, motif)))
    return 0

if __name__ == "__main__":
    main()
