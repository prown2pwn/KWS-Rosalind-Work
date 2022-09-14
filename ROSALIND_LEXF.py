import itertools

###OPEN FILE FUNCTION
def OpenFile(file):
    with open(file, 'r') as f:
        return[l.strip() for l in f.readlines()]
### Making file usable for the purpose
rawData = OpenFile('rosalind_lexf.txt')

dataList = []


for line in rawData:
    if line.isdigit() == False:
        noSpace = line.replace(' ', '')
        for char in noSpace:
            dataList.append(char)
        print(dataList)
    else:
        n = int(line)
        # print(n)

def Organize(dataList, n):
    combination = itertools.product(dataList, repeat = n)
    product = []
    for i, j in enumerate(list(combination)):
        comb = ''
        for char in j:
            comb += str(char)
        product.append(comb)
    sortProduct = sorted(product)
    print(sortProduct)
    return sortProduct
rosalind = Organize(dataList, n)

### Rosalind Answer Format
for char in rosalind:
    print(char)