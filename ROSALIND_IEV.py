#ROSALIND given chart
genotype = {1:'AA-AA', 2:'AA-Aa', 3: 'AA-aa', 4: 'Aa-Aa', 5:'Aa-aa', 6:'aa-aa'
            }
#couple pair as key and chance of dominant offspring as a value
dominantChance = {'AA-AA':1, 'AA-Aa':1, 'AA-aa':1, 'Aa-Aa':0.75, 'Aa-aa':0.5, 'aa-aa':0
                  }
#number of couple corresponding to ROSALIND genotype chart in order.
couple = [17154, 16912 , 19742 , 18368 , 17595 , 17675]
#calculate chance of dominant offspring with given population of genotype couple.
dominant = 0
for i in range(1,7):
    dominant += dominantChance[genotype[i]] * couple[i-1] * 2
print(dominant)

