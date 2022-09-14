def readInput(file):
    with open(file, 'r') as f:
        return[l.strip() for l in f.readlines()]
input = readInput('test.txt')

seqlist = sorted(input)
s = seqlist[0]
t = seqlist[1]
superseq = s
print(t)
print(s)
print(len(s), len(t))
n = 0
k = n + 1

# for i in range(len(s)):
#     if i >= len(t):
#         break
#     j = i + 1
#     motif = t[i]
#     for k in range(len(s)):
#         l = k + 1
#         if motif == s[k]:
#             motif = t[i:j]
#             sample = s[k:l]
#             if motif == sample:
#                 superseq = superseq[:k] + motif + superseq[k:]
#                 break
# print(superseq)

# for i in range(len(t)):
#     for j in range(i + 1, len(s) + 1):
#         motif = t[i]
#         sample = s[j-1:j]
#         if motif == sample:
#             motif = t[i:j]
#             sample = s[j-1: j +1]
def splicedmotif(s,t):
    print(len(s),len(t))
    lengths = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
# print(lengths)
# creates array of len(s) containing arrays of len(t) filled with 0
    for i, x in enumerate(s):
        # print(x)
        for j, y in enumerate(t):
            # print(x, y)
            if x == y:
                lengths[i + 1][j + 1] = lengths[i][j] + 1
            else:
                lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])

# print(lengths)



    spliced_motif = ''
    x, y = len(s), len(t)
    while x * y != 0:
        if lengths[x][y] == lengths[x - 1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y - 1]:
            y -= 1
        else:
            spliced_motif = s[x - 1] + spliced_motif
            x -= 1
            y -= 1
    print(spliced_motif)
    return spliced_motif
# splicedmotif(s,t)

# def superseq(s,t):
#     subseq = splicedmotif(s,t)
#     superseq = ''
#     for nt in subseq:
#         for i in range(len(s)):
#             if s[i] != nt:
#                 superseq += s[i]
#         for j in range(len(t)):
#             if t[j] != nt:
#                 superseq += t[j]
#         superseq += nt
#     print(superseq)
#     return superseq
# superseq(s,t)
def scs(s,t):
    subseq = splicedmotif(s,t)
    superseq = ''
    i, j = 0, 0
    for nt in subseq:
        seq1 = s[i]
        seq2 = t[j]
        if i < len(s):
            while s[i] != nt:
                superseq += s[i]
                i += 1
            i += 1
        if j < len(t):
            while t[j] != nt:
                superseq += t[j]
                j += 1
            j += 1
        superseq += nt
    if i < len(s):
        superseq += s[i:]
    if j < len(t):
        superseq += t[j:]
    return(superseq)
print(scs(s,t))