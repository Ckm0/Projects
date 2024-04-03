import random
l = [1,2,3,4,5,6,7,8,9]
f = lambda a,b : print(a*10+b)
f1 = lambda : random.shuffle(l)
f1()
print(l) 