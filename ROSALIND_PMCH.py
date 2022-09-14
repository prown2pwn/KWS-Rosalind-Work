from math import factorial
##OPEN FASTAFILE FUNCTION
def readFASTAFile(file):
    with open(file, 'r') as f:
        return[l.strip() for l in f.readlines()]
### Making FASTA file usable for the purpose
FASTAFile = readFASTAFile('rosalind_pmch.txt')

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

# def perfect_match(FASTALIST):
#     UA_pair = []
#     GC_pair = []
#     seq = FASTALIST[0]
#     for i in range(len(seq)):
#         for j in range(i + 1, len(seq)):
#             if seq[i] == 'U':
#                 if [i, j] or [j, i] not in UA_pair:
#
#                     if seq[j] == 'A':
#                         UA_pair.append([i, j])
#             if seq[i] == 'A':
#                 if [i, j] or [j, i] not in UA_pair:
#                     if seq[j] == 'U':
#                         UA_pair.append([i, j])
#             if seq[i] == 'G':
#                 if [i, j] or [j, i] not in GC_pair:
#                     if seq[j] == 'C':
#                         GC_pair.append([i, j])
#             if seq[i] == 'C':
#                 if [i, j] or [j, i] not in GC_pair:
#                     if seq[j] == 'G':
#                         GC_pair.append([i, j])
#     return UA_pair, GC_pair
#
# print(FASTAList[0])
# print(perfect_match(FASTAList))

# The Code above only find matches but not perfect matches.
# Took different approach to solve this problem. Given [G,C] and [U,A] don't share nodes, we can safely say
# GC graph and UA graph is two different graph and multiply p match for each graph.
# # of perfect match for each graph will be # of G/C and # of U/A factorial, given # of nodes that match are same
# # of G == # of C, # of U == # of A
sequence = FASTAList[0]
AU = 0
GC = 0
for nt in sequence:
    if nt == 'A':
        AU += 1
    elif nt == 'G':
        GC += 1

matchings = factorial(AU) * factorial(GC)
print(matchings)