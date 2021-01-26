from random import randint
num = input('Number of times to flip coin: ')
flips = [randint(0,1) for r in range(num)]
results = []
for object in flips:
        if object == 0:
            results.append('Heads')
        elif object == 1:
            results.append('Tails')
print (results)
