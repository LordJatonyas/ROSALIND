import sys
from Bio import SeqIO

def is_substring(find, strands):
    if len(strands) < 1 and len(find) < 1:
        return False
    for i in range(len(strands)):
        if find not in strands[i]:
            return False
    return True

def longest_substring(strands):
    substring = ""
    if len(strands) > 1 and len(strands[0]) > 0:
        for i in range(len(strands[0])):
            for j in range(len(strands[0]) - i + 1):
                if j > len(substring) and is_substring(strands[0][i:i+j], strands):
                    substring = strands[0][i:i+j]
    return substring

def main():
    if len(sys.argv) != 2:
        print("Usage: python graph.py [TXT file]")
        return 1
    strands = list()
    for strand in SeqIO.parse(sys.argv[1], "fasta"):
        strands.append(strand.seq)
    res = longest_substring(strands)
    print(res)
    return 0

if __name__ == "__main__":
    main()
