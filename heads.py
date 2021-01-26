import random

Heads = 1
Tails = 2

def coin():
      flip = random.randint(1,2)
      if flip == 1:
         print ("It is Heads")
      else:
         print("It is Tails")

def times():
   for x in range(10):
      print(coin(),"\n")

times()
