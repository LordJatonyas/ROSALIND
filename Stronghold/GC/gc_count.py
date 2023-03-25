import sys
from Bio import SeqIO

def gc_count(d):
    gc = 0
    max_gc_content = 0
    for i, v in d.items():
        for c in v:
            if c == "C" or c == "G":
                gc += 1
        gc_content = gc / len(v)
        d[i] = gc_content
        max_gc_content = max(gc_content, max_gc_content)
        gc = 0

    for a, b in d.items():
        if b == max_gc_content:
            return a, b * 100
    return "", 0

def main():
    if len(sys.argv) != 2:
        print("Usage: python gc_count.py [TXT file]")
        return 1
    dna_map = dict()
    for record in SeqIO.parse(sys.argv[1], "fasta"):
        dna_map[record.id] = record.seq
    name, gc_content = gc_count(dna_map)
    print(f'{name}\n%.6f' % gc_content)
    return 0

if __name__ == "__main__":
    main()
