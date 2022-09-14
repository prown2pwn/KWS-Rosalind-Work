import math

#Read input file and store DNA seq into string and log(GC) in to list
def readInput(file):
    with open(file, 'r') as f:
        return[l.strip() for l in f.readlines()]
input = readInput('rosalind_prob (1).txt')
seq = ''
arrayX = []
for line in input:
    if 'A' and 'C' and 'G' and 'T' in line:
        seq = line
    else:
         arrayX = [float(i) for i in line.split()]

#assign output list as arrayY
arrayY = []
#calculating event output given 'log(a x b) = log(a) + (b)'
for prob in arrayX:
    #assign x
    x = prob
    #assign y as canstant
    y = 0
    #calculated probability
    probability = {
        'A': (1 - x) / 2,
        'C': x/2,
        'G': x/2,
        'T': (1 - x) / 2
    }

    for chance in seq:
        y = y + math.log10(probability[chance])
    arrayY.append(y)
print(arrayY)
#output for ROSALIND ANSWER format
output = ''
for i in arrayY:
    output = output + ' ' + str(i)
print(output)