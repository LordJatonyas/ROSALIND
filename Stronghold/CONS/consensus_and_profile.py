import sys
from Bio import SeqIO

def profile_matrix(strands):
    ACGTs = list()
    for j in range(len(strands[0])):
        ACGTs.append([0, 0, 0, 0])
        for i in range(len(strands)):
            if strands[i][j] == "A":
                ACGTs[-1][0] += 1
            elif strands[i][j] == "C":
                ACGTs[-1][1] += 1
            elif strands[i][j] == "G":
                ACGTs[-1][2] += 1
            elif strands[i][j] == "T":
                ACGTs[-1][3] += 1
    return ACGTs

def consensus(ACGTs):
    res = ""
    for ACGT in ACGTs:
        most_common = "A"
        most_count = ACGT[0]
        if most_count < ACGT[1]:
            most_count = ACGT[1]
            most_common = "C"
        if most_count < ACGT[2]:
            most_count = ACGT[2]
            most_common = "G"
        if most_count < ACGT[3]:
            most_common = "T"
        res += most_common
    return res

def main():
    if len(sys.argv) != 2:
        print("Usage: python consensus_and_profile.py [TXT file]")
        return 1
    strands = list()
    for strand in SeqIO.parse(sys.argv[1], "fasta"):
        strands.append(strand)
    nucleobase_counts = profile_matrix(strands)
    print(consensus(nucleobase_counts))
    adenine = list()
    cytosine = list()
    guanine = list()
    thymine = list()
    for n in nucleobase_counts:
        adenine.append(n[0])
        cytosine.append(n[1])
        guanine.append(n[2])
        thymine.append(n[3])
    print("A: " + " ".join(str(a) for a in adenine))
    print("C: " + " ".join(str(c) for c in cytosine))
    print("G: " + " ".join(str(g) for g in guanine))
    print("T: " + " ".join(str(t) for t in thymine))
    return 0

if __name__ == "__main__":
    main()
