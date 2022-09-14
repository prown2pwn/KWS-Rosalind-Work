###OPEN FASTAFILE FUNCTION
def readFASTAFile(file):
    with open(file, 'r') as f:
        return[l.strip() for l in f.readlines()]
### Making FASTA file usable for the purpose
FASTAFile = readFASTAFile('rosalind_revp.txt')

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

seq = FASTAList[0]


def CompDNA(seq):
    compDna = ""
    ###read through seq and pair nt and store in as compdna
    for nt in seq:
        if nt == "A":
            compDna += "T"
        if nt == "T":
            compDna += "A"
        if nt == "G":
            compDna += "C"
        if nt == "C":
            compDna += "G"
    # print(compDna)
    return(compDna)
### compare seq and comseq to see if they are mirrored
# print(seq)
compSeq = CompDNA(seq)
test = ''

for i in range(len(seq)):
    for j in range(i + 4, len(seq) + 1):
        test = ''.join(reversed(compSeq[i:j]))
        if len(test) > 12:
            break
        if seq[i:j] == test:
            print(i + 1, len(test))

