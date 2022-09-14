##OPEN FASTAFILE FUNCTION
def readFASTAFile(file):
    with open(file, 'r') as f:
        return[l.strip() for l in f.readlines()]
### Making FASTA file usable for the purpose
FASTAFile = readFASTAFile('rosalind_grph.txt')

FASTADict = {}

FASTAList = []

FASTALabel = ""

for line in FASTAFile:
    if '>' in line:
        FASTALabel = line.replace('>', '')
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line
for curValue in FASTADict.values():
    FASTAList.append(curValue)
# print(FASTAList)
# print(FASTADict)

# assign prefix and suffix
prefix = {key: value[0:3] for (key, value) in FASTADict.items()}
suffix = {key: value[-3:] for (key, value) in FASTADict.items()}
match = []
# print(prefix)
# print(suffix)

# find match
for pre in prefix:
    for suf in suffix:
        if pre != suf:
            if prefix[pre] == suffix[suf]:
                match.append(suf + ' ' + pre)

# print for ROSALIND
for answer in match:
    print(answer)