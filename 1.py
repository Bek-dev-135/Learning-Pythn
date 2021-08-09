# import sys
#
#
# import random
#
# num=random.randint(1,10)
#
# i=int(sys.argv[1])
# b=True
# while b:
#     if i>0 and i<10:
#
#         if i==num :
#             print('you genius')
#             b=False
#         else:
#             print('try again')
#             b = False
#     else:
#         print('enter a number between 1-10')


import unittest
import main


class TestMain(unittest.TestCase):
    def tester1(self):
        answer=5
        random=5
        result= main.ranndomize(answer,random)
        self.assertTrue(result)


unittest.main()


