seq1 = 'CCGGATGTGGCCTTGTGGCCGTTGTGGCCCCGCGTCCCTTGATGTGGCCTGTGGCCTGTGGCCTGTGGCCTAGAGACGCTATGTGGCCCAGTAGTGTGGCCATGTGGCCAAGCGGTGTGGCCTCTGAACATGTAGTGGTTGTGGCCTTTGTGTGGCCTGTGGCCACCTGTGGCCTAATGTGGCCACTGTGGCCTATGTGGCCTGTGGCCAGATGTGGCCCTGTGGCCGGGTTGTGGCCTCTTTGTGGCCTCTGTGGCCTGTGGCCTGTGGCCATGTGGCCTGGTGTGGCCTTAGTGTGGCCATGAGTTGTGGCCTGATGTGGCCCTGTGGCCTTGTGGCCAAACCTGTGGCCGTGGTGTTGTGTGGCCTGGTGCTTGTGGCCTGTGGCCTGTGGCCCGAGTGTGGCCCTGTGGCCTATTGTGGCCATTGTGGCCCACTTGTGGCCTGTGGCCTGCTGTGGCCTGTGGCCTGTGGCCATTCGCATAAGGCTGTGGCCTGTGGCCCTGTGGCCAAGTGTGGCCGTGTGGCCATGTGGCCGTCGGTGGATGCTATATTGTGGCCCCATTTGTGGCCTGTGGCCTGCACCGATGTGGCCGTGTGGCCTGTGGCCGGGGGGAGGGCTTGTGGCCGTGTGGCCGGAGACGTACTGATGTGGCCGTGTGGCCCGTTGTGGCCTTGTGGCCGTTGTGGCCTGTGGCCAACTATTGTGGCCCCCTGTGGCCTGTGGCCTGTGGCCTAACTGTGGCCTTGTGGCCTGTGGCCTGTGTGGCCGTGATAGCTCTGTGTGGCCTCAGACTGTGGCCTGTGGCCTGTGGCCGGCTTGTGGCCTGTGGCCTGTGGCCCCCCGGCGCTTTATCTGTGGCC'
seq2 = 'TGTGGCCTG'
motif = []
#finding seq2 in seq1, and record position in motif list.
for i in range(len(seq1)):
    if seq1[i:i + len(seq2)] == seq2:
        motif.append(i+1)
output = ' '.join(str(m) for m in motif)
print(output)
