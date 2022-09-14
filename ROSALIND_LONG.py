# OPEN FASTAFILE FUNCTION
def readFASTAFile(file):
    with open(file, 'r') as f:
        return[l.strip() for l in f.readlines()]
# Making FASTA file usable for the purpose
FASTAFile = readFASTAFile('rosalind_long.txt')

FASTADict = {}

FASTAList = []

FASTALabel = ""

for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line
for value in FASTADict.values():
    FASTAList.append(value)

# superstring = FASTAList[0]
#
# for i in range(len(FASTAList) + 1):
#     if i + 1 >= len(FASTAList):
#         break
#     test = FASTAList[i + 1]
#
#     for j in range(len(superstring)):
#         glue = ''
#         location = 0
#         match = []
#         position = {}
#         for k in range(j + 1, len(superstring) + 1):
#             if test in superstring:
#                 break
#             else:
#                 if test[j:k] in superstring:
#                     position[k] = test[j:k]
#                     match.append(test[j:k])
#         if len(match) > 0:
#             # print(position)
#             glue = max(match, key = len)
#             # print(glue)
#             keys = list(position.keys())
#             vals = list(position.values())
#             location = keys[vals.index(glue)]
#             superstring = superstring + test[location::]
#             break
# print(superstring)

# ###commented code does work for the example problem, but doesn't work with actual problem due to logic error. for ex
# ### max(match, key = len) != suffix/prefix (actual spot we're looking for)

def get_superstring(FASTAList, superstring=''):
    # check if FASTAList is good to use.
    if len(FASTAList) == 0:
        return superstring
    # check if superstring is assigned. By popping out the first for the test we don't have to run for loop index + 1.
    # also by doing this, code re-run itself over and over until there is nothing to compare.
    elif len(superstring) == 0:
        superstring = FASTAList.pop(0)
        return get_superstring(FASTAList, superstring)
    # actual test code to look for suffix/prefix, and glue the overlap to superstring.
    else:
        for curr_index in range(len(FASTAList)):
            curr_read = FASTAList[curr_index]
            curr_read_len = len(curr_read)
            # //2 since we're only checking front and back for prefix and suffix.
            for test in range(curr_read_len // 2):
                overlap_len = curr_read_len - test
                # str.startswith function look for suffix of curr_read if match
                # curr_read + superstring
                if superstring.startswith(curr_read[test:]):
                    FASTAList.pop(curr_index)
                    return get_superstring(FASTAList, curr_read[:test] + superstring)
                # str.endswith function look for prefix of curr_read if match
                # superstring + curr_read
                if superstring.endswith(curr_read[:overlap_len]):
                    FASTAList.pop(curr_index)
                    return get_superstring(FASTAList, superstring + curr_read[overlap_len:])
print(get_superstring(FASTAList))
