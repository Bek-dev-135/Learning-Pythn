import sys


import random

num=random.randint(1,2)

i=int(sys.argv[1])
b=True
while b:
    if i==num:
        print('you genius')
        b=False
    else:
        print('try again')
        b = False
