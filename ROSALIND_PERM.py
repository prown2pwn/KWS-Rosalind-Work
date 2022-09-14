import math
import itertools
import re
n = 6
print(math.factorial(n))
perm = itertools.permutations(list(range(1, n + 1)))

#ROSALIND OUTPUT
rosalind = []

for i in perm:
    rosalind.append(re.sub('[(,)]','', str(i)))
for j in rosalind:
    print(j)