import sys

RNA_CODON_TABLE = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S",
                   "UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y", "UAC": "Y",
                   "UAA": "end", "UAG": "end", "UGU": "C", "UGC": "C", "UGA": "end",
                   "UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
                   "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H",
                   "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R",
                   "CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I", "AUA": "I",
                   "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                   "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S",
                   "AGC": "S", "AGA": "R", "AGG": "R", "GUU": "V", "GUC": "V",
                   "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A",
                   "GCG": "A", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
                   "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

def translate(s):
    res = ""
    for i in range(0, len(s), 3):
        if s[i:i+3] in RNA_CODON_TABLE:
            if RNA_CODON_TABLE[s[i:i+3]] != "end":
                res += RNA_CODON_TABLE[s[i:i+3]]
            else:
                return res
    return res

def main():
    if len(sys.argv) != 2:
        print("Usage: python translate.py [TXT file]")
        return 1
    f = open(sys.argv[1], "r").read()
    print(translate(f))
    return 0

if __name__ == "__main__":
    main()
