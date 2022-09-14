###OPEN FASTAFILE FUNCTION
def readFASTAFile(file):
    with open(file, 'r') as f:
        return[l.strip() for l in f.readlines()]
### Making FASTA file usable for the purpose
FASTAFile = readFASTAFile('rosalind_cons.txt')

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

length = sorted(FASTAList)
print(len(length[0]),len(length[-1]))
#assaign the longest DNA seq length for the loop purpose
maxlen = length[-1]
FASTAMatrix = []
#count each nt in each seq in list of seq and store as dictionary format in FASTAMatrix list.
for i in range(len(maxlen)):
    conDic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for list in FASTAList:
        if i > len(list):
            break
        nt = list[i]
        if nt in conDic:
            conDic[nt] += 1
        else:
            conDic[nt] = 1
    FASTAMatrix.append(conDic)
#store the key of the maximum value of the nt count into consensus string.
consensus = ''
for nuc in FASTAMatrix:
    consensus += (max(nuc, key=nuc.get))


print(consensus)
