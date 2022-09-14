dnaSeq = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"


compDna = ""
###read through seq and pair nt and store in as comp_dna
for nt in dnaSeq:
    if nt == "A":
        compDna += "T"
    if nt == "T":
        compDna += "A"
    if nt == "G":
        compDna += "C"
    if nt == "C":
        compDna += "G"
print(compDna[::-1])