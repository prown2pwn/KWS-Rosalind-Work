###OPEN FASTAFILE FUNCTION
def readFASTAFile(file):
    with open(file, 'r') as f:
        return[l.strip() for l in f.readlines()]
### Making FASTA file usable for the purpose
FASTAFile = readFASTAFile('rosalind_orf.txt')

FASTADict = {}

FASTAList = []

FASTALabel = ""

for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line
for curValue in FASTADict.values():
    FASTAList.append(curValue)

### dictionary for transalation
DNA_Codons = {
    # 'M' - START, '_' - STOP
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "M",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "_", "TAG": "_", "TGA": "_"
}

seq = FASTAList[0]
###Finding Comp DNA
def compDNA(seq):
    comp_dna = ""

    for n in seq:
        if n == "A":
            comp_dna += "T"
        if n == "T":
            comp_dna += "A"
        if n == "G":
            comp_dna += "C"
        if n == "C":
            comp_dna += "G"
    # print(comp_dna[::-1])
    return comp_dna[::-1]


###TRANSLATE
def ORF(seq, initialpos = 0):
    protein = []
    startP = []
    rstartP = []
    rseq = compDNA(seq)
###Finding start codons position in DNA
    for pos in range(initialpos, len(seq) - 2, 1):
        if DNA_Codons[seq[pos:pos + 3]] == 'M':
            startP.append(pos)
###Finding start condons in Comp DNA
    for rpos in range(initialpos, len(rseq) - 2, 1):
        if DNA_Codons[rseq[rpos:rpos + 3]] == 'M':
            rstartP.append(rpos)
###Translate DNA to AA and added to protein list
    for startValue in startP:
        fragment = ''

        for curValue in range(startValue, len(seq)-2, 3):
            key = DNA_Codons[seq[curValue:curValue+3]]
###End Codon for DNA
            if key == '_':
                protein.append(fragment)
                break
            fragment += key
###Translate Comp DNA to AA and added to protein list
    for revStartValue in rstartP:
        revFragment = ''

        for revCurValue in range(revStartValue, len(seq)-2, 3):
            revKey = DNA_Codons[rseq[revCurValue:revCurValue+3]]
###End Codon for Comp DNA
            if revKey == '_':
                protein.append(revFragment)
                break
            revFragment += revKey
    # print(protein)
    return protein
###OUTPUT for ROSALIND answer form
print(set(ORF(seq)))
for character in set(ORF(seq)):
    print(character)