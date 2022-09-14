with open('rosalind_mrna.txt', 'r') as f:
    protein = f.read().strip()

RNA_Codons = {
    # 'M' - START, '_' - STOP
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UGU": "C", "UGC": "C",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UUU": "F", "UUC": "F",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAU": "H", "CAC": "H",
    "AUA": "I", "AUU": "I", "AUC": "I",
    "AAA": "K", "AAG": "K",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUG": "M",
    "AAU": "N", "AAC": "N",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UGG": "W",
    "UAU": "Y", "UAC": "Y",
    "UAA": "_", "UAG": "_", "UGA": "_"
}
modulo = 1000000

### Finding all the possible codon for each aa that match.
def RevTrans(protein):
    mRNAs = [[] for i in range(len(protein))]
    for i in range(len(protein)):
        aa = protein[i]
        for key in RNA_Codons:
            if RNA_Codons[key] == aa:
                mRNAs[i].append(key)
    return mRNAs
RevTrans(protein)
###calculating probability by multiplying all possible combination. Times 3 for 3 different end codon.
possible = 1
for i in range(len(protein)):
    possible = possible * len(RevTrans(protein)[i])

possible = 3 * possible
### Modulo 1000000
print(possible % modulo)


