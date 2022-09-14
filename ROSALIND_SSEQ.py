###OPEN FASTAFILE FUNCTION
def readFASTAFile(file):
    with open(file, 'r') as f:
        return[l.strip() for l in f.readlines()]
### Making FASTA file usable for the purpose
FASTAFile = readFASTAFile('rosalind_sseq.txt')

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

def splicedmotif():
    BIGSeq = FASTAList[0]
    SMALLSeq = list(FASTAList[1])
    ###Identifying indices position
    indicesPosition = []
    initialPosition = 0

    #find position where match
    for index in range(0, len(BIGSeq) - 1):
        if BIGSeq[index] == SMALLSeq[initialPosition]:
            initialPosition += 1
            indicesPosition.append(index + 1)

            if initialPosition >= len(SMALLSeq):
                break

    returnValue = ''
    #ANSWER FORM FOR ROSALIND
    for digit in indicesPosition:
        returnValue += str(digit)
        returnValue += ' '
    print(returnValue)
    return(indicesPosition)
splicedmotif()

