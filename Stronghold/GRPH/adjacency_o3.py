import sys
from Bio import SeqIO

def adjacency_list(nodes):
    res = ""
    for x in nodes:
        for y in nodes:
            if x[0] != y[0]:
                if x[1][-3:] == y[1][:3]:
                    res += f'{x[0]} {y[0]}\n'
    return res

def main():
    if len(sys.argv) != 2:
        print("Usage: python graph.py [TXT file]")
        return 1
    node_list = list()
    for strand in SeqIO.parse(sys.argv[1], "fasta"):
        node_list.append((strand.id, strand.seq))
    res = adjacency_list(node_list)
    print(res)
    return 0

if __name__ == "__main__":
    main()
