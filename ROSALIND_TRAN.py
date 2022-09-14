###OPEN FASTAFILE FUNCTION
def readFASTAFile(file):
    with open(file, 'r') as f:
        return[l.strip() for l in f.readlines()]
### Making FASTA file usable for the purpose
FASTAFile = readFASTAFile('rosalind_tran.txt')

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

#IDENTIFY PURINE AND PYRIMIDINE
purine = ['A', 'G']
pyrimidine = ['C', 'T']

seq1 = FASTAList[0]
seq2 = FASTAList[1]
#IDENTIFYING HAMMERING DISTANCE/MUTATION POINT.
n=0
ham = ''
mPoint = []
for char in seq1[0::]:
    if seq2[n] != char:
        ham += char
        mPoint.append(n)
    n += 1
print(mPoint)
#CHECK WHICH TYPE OF MUTATION
tranCounter = 0
travCounter = 0

for i in mPoint:
    if seq1[i] in purine and seq2[i] in purine:
        tranCounter += 1
    elif seq1[i] in purine and seq2[i] in pyrimidine:
        travCounter += 1
    elif seq1[i] in pyrimidine and seq2[i] in pyrimidine:
        tranCounter += 1
    elif seq1[i] in pyrimidine and seq2[i] in purine:
        travCounter += 1

print(tranCounter, travCounter)

print(tranCounter/travCounter)



