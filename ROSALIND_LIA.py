import math
#define
generation = 7
population = 2**(generation)
punnetProb = 0.25
tomGenotype = 33
#Binomial Distribution Formula given all Punnet SQ give .25 chance for AaBb
def AaBbProb(tomGenotype):
    probability = 0
    for i in range(tomGenotype, population + 1):
        prob = (math.factorial(population)/
                (math.factorial(i) * math.factorial(population - i)) * (0.25**i) * (0.75**(population - i)))
        probability += prob
    print(probability)
    return probability
AaBbProb(tomGenotype)