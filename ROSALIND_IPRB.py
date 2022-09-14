prob = {'kk' : 1, 'km' : 1, 'kn' : 1, 'mm' : 0.75, 'mn' : 0.5, 'nn' : 0}
k = 28
m = 21
n = 17
alle = 2 * (k + m + n)
dominantA = 2 * k + m
recessiveA = 2 * n + m
dominant = k + m
recessive = n
pop = k + m + n

event = k/pop + (m/pop * k/(pop-1)) + (m/pop * (m-1)/(pop-1) * 0.75) +(m/pop * n/(pop-1) * 0.5) + (n/pop * m/(pop-1) * 0.5) + (n/pop * k/(pop-1))

print(event)
### OH WOW THIS CODE IS TERRIBLE - by me (April,12,2022) I really need to make this better.