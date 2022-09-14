n = 4
k = 1
def fib(n, k):
    mature, child = 1, 1
    for i in range(2, n):
        child, mature = mature, mature + (child * k)
    return mature
print(fib(n, k))


numMonths = 5
numOffspring = 3
def rabbitPairs(numMonths, numOffspring):
    if (numMonths == 1):
        return 1
    elif (numMonths == 2):
        return 1
    oneGen = rabbitPairs(numMonths - 1, numOffspring)
    twoGen = rabbitPairs(numMonths - 2, numOffspring)
    return (oneGen + (twoGen * numOffspring))
print(rabbitPairs(n, k))

# def fib(n, k):
#     previous1, previous2 = 1, 1
#     for i in range(2, n):
#         previous1, previous2 = previous2, previous1 * k + previous2
#     return previous2
#
# print(fib(n, k))

