# print(2+4)
# print(type(2+4))
# print(2**3)
# print(2//4)
# print(3//4)
# print(5//4)
# print(round(3.4))
# print(abs(-10))
# print("Hello {}, your balance is {}.".format("Cindy", 50))
#
# print("Hello {0}, your balance is {1}.".format("Cindy", 50))
#
# print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))
#
# print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))

#
# str= "01234567"

# [strat:stop:step over]
# print (str[0:3])
# print (str[0:7:2])
#
# quote="to be or not to be"
#
# print (quote.upper())
# print (quote.capitalize())
# print (quote.find("be"))
# print (quote.replace("be","me"))

# user=input("user name")
# ps=input ("password")
#
# print (f"{user} your password {'*' * len(ps)} is  {len(ps)} letters long")

# i=10
# b=10
# while (i>1):
#     astrik= (2*(10-b))+1
#     print (f"{' '* i} {'*'*astrik}")
#     i-=1
#     b-=1
# c=1
# while(c<3):
#     print(f"{' '* 8} {'*'*5}")
#     c+=1

# basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
# print(basket[1][1][0])
#
# basket = ['a','b', 'c', 'd', 'e'];
# print ("c" in basket)

# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
#
# # 1. Remove the Banana from the list
#
# # 2. Remove "Blueberries" from the list.
#
# # 3. Put "Kiwi" at the end of the list.
#
# # 4. Add "Apples" at the beginning of the list
#
# # 5. Count how many apples in the basket
#
# # 6. empty the basket
# basket.remove("Banana")
# basket.pop()
# basket.append("kiwi")
# basket.insert(0,'Apples')
# print(basket)
# print(basket.count("Apples"))
# basket.clear()
# print(basket)

#
# sentence= '!'
# new_sentence= sentence.join(['hi', 'my','name', 'is', 'john'])
# print (new_sentence)
#
#
# new_sentence1= "!".join(['hi', 'my','name', 'is', 'john'])
# print (new_sentence1)
#
#
# #fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
# friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
#
# friends.append('Stanley')
# friends.sort()
# print(friends)
#
# friends1 = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
#
# new_friend = ['Stanley']
# friends1+= new_friend
# friends1.sort()
# print(friends1)

#
# a,*b,c=[1,2,3,4,5,6,7]
# print(a)
# print(b)
# print(c)
#
#
# dictionary={
#     'name': [1,2,3],
#     'greeting':'hello',
#     'age': 20
# }
# print ( 'name' in dictionary.keys())
# print ( 'hello' in dictionary.values())


# 1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

# 2 iterate and print all the keys in the above user.

# 3 Add a new weapon to your user

# 4 Add a new key to include 'is_banned'. Set it to false

# 5 Ban the user by setting the previous key to True

# 6 create a new user2 my copying the previous user and update the age value and username value.

#
# dictionary={
#     'age':20,
#     'username':"bek",
#     'weapons':['sword', "dagger"],
#     'is_active': True,
#     'clan': 'nots'
# }
# print ( dictionary.keys())
# #dictionary.update({'weapons':['sworrd', "dagger",'saber']})
# dictionary['weapons'].append('shield')
# print ( dictionary)
# dictionary.update({'is_banned':False})
# print ( dictionary)
# dictionary.update({'is_banned':True})
# print ( dictionary)
#
# user2=dictionary.copy()
# user2.update({'age':45})
# user2.update({'username':'toro'})
# # user2.update({'age': 45, 'username': 'Toro'})
# print ( user2)

# #Scroll to bottom to see solution
# # You are working for the school Principal. We have a database of school students:
# school = {'Bobby','Tammy','Jammy','Sally','Danny'}
#
# #during class, the teachers take attendance and compile it into a list.
# attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']
#
# #using what you learned about sets, create a piece of code that the school principal can use to immediately
# # find out who missed class so they can call the parents. (Imagine if the list had 1000s of students.
# # The principal can use the lists generated by
# # the teachers + the school database to use python and make his/her job easier): Find the students
# # that miss class!
#
# print(school.difference(attendance_list))
# #Solution: Notice how we don't have to convert the attendance_list to a set...it does it for you.
# #print(school.difference(attendance_list))
#
# #Ternary Operator
# is_tall= True
# print('Tall' if is_tall else 'short')
#
# user={
#     'name': "Abed",
#     'age ': 20,
#     'is racist': True
#
# }
#
# for item in user:
#     print (item)
#
# for item in user.items():
#     print (item)
#
# for item in user.keys():
#     print (item)
#
# for item in user.values():
#     print(item)
#
# for key, value in user.items():
#     print (key, value)
#
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
# i=0
# string=''
# while i<6:
#     j = 0
#     while j<7:
#         if picture[i][j]==0:
#             print(" ", end='')
#         else:
#             print("*", end='')
#         j+=1
#     print('')
#
#
#     i+=1
#
#
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#
# for char in some_list:
#     checker=some_list.count(char)
#     if (checker>1):
#         print (char+ ' is a duplicate')
#         some_list.remove(char)
#
#
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#
# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#             duplicates.append(value)
#
# print(set(duplicates))

#
# # Function 101
# def say_hello(name, emoji):
#     print(f'hello {name} {emoji}')
#
# # positional argument
# say_hello('bek',':)')
#
# #keyword argument
#
# say_hello(emoji=':)',name='bek')
#
# #default parametes
# def say_hello(name="darth", emoji=':('):
#     print(f'hello {name} {emoji}')
#
# # positional argument
# say_hello('bek',':)')
# say_hello()
# say_hello('happy')
# say_hello(emoji=':0')

# age = input("What is your age?: ")
#
# if int(age) < 18:
# 	print("Sorry, you are too young to drive this car. Powering off")
# elif int(age) > 18:
# 	print("Powering On. Enjoy the ride!");
# elif int(age) == 18:
# 	print("Congratulations on your first year of driving. Enjoy the ride!")

# 1. Wrap the above code in a function called checkDriverAge(). Whenever you call t
# his function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

# 2 Instead of using the input(). Now, make the checkDriverAge() function accept an
# argument of age, so that if you enter:
# checkDriverAge(92);
# it returns "Powering On. Enjoy the ride!"
# also make it so that the default age is set to 0 if no argument is given.

# def checkDriverAge(age=0):
#     p=""
#     if int(age) < 18:
#         p= "Sorry, you are too young to drive this car. Powering off"
#     elif int(age) > 18:
#         p="Powering On. Enjoy the ride!"
#     elif int(age) == 18:
#         p= "Congratulations on your first year of driving. Enjoy the ride!"
#     return print(p)
#
# checkDriverAge(95)

# def highest_even(li):
#     even=[]
#     for item in li:
#         if item%2==0:
#             even.append(item)
#     print (even)
#     j=1
#     highet = even[0]
#     while j<len(even):
#
#         if even[j]>highet:
#                highet=even[j]
#                j+=1
#
#         else:
#
#             j+=1
#     return print(highet)
#
# highest_even([10,8,5,3,7,2,11,12,14])


# class playerCharacter:
#     membership= True
#     def __init__(self, name ,age):
#         self.a=name
#         self.b=age
#
# player1= playerCharacter('Cindy', 20)
# player1.membership= False
#
# print(player1.a)
# print(player1.membership)

# 1 Instantiate the Cat object with 3 cats


# 2 Create a function that finds the oldest cat


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# def oldestCat(list):
#         return max(list)
#
# cat1 = Cat('tokyo', 3)
# cat2 = Cat('simp', 2)
# cat3 = Cat('toro', 4)
#
#
#
# cats = [cat1.age, cat2.age, cat3.age]
#
#
# print(f"The oldest cat is {oldestCat(cats)} years old.")


# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def adding(cls, num1, num2):
#         return cls('ted', num1+num2)
#
# pcat3=Cat.adding(2,3)
#
# print(pcat3.age)

# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Garfild(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# simon=Simon('simon', 4)
# sally=Sally('sally', 6)
# garfield=Garfild('garfield', 3)
# my_cats= [simon,sally,garfield]
#
# my_pets= Pets(my_cats)
# my_pets.walk()
#
# #1 Add nother Cat
#
# #2 Create a list of all of the pets (create 3 cat instances from the above)
#
#
# #3 Instantiate the Pet class with all your cats use variable my_pets
#
# #4 Output all of the cats walking using the my_pets instance
#
# class SuperList(list):
#
#     def __len__(self):
#         return 1000
#
# super_list=SuperList()
# print(len(super_list))


# def func1(li):
#     new_list=[]
#     for item in li:
#         new_list.append(item*2)
#
#     return new_list
#
# print(func1([1,2,3,4]))


# def func1(item):
#     return item*2
#
# print(list (map(func1, [1,2,3,4])))
#
# def func1(item):
#     return item*2
#
# def odd(ii):
#     return ii % 2== 0
#
# print(list (filter(odd, [1,2,3,4])))


# from functools import reduce
#
# #1 Capitalize all of the pet names and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']
# def capitalize(item):
#     return item.upper()
#
# print(list(map(capitalize,my_pets)))
#
# #2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5,4,3,2,1]
# my_numbers.sort()
#
# print (list(zip(my_numbers, my_strings)))
#
# # better to use
# #
# # print(list(zip(my_strings, sorted(my_numbers))))
# #
# # because sorted() doesnt affect the original list
#
#
# #3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]
#
# def passed(pp):
#     return pp>50
#
# print(list(filter(passed,scores)))
#
# #4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
#
# def accumulator(acc, item):
#     return acc+item
#
# print(reduce(accumulator, (my_numbers+ scores)))
#
# my_pets = ['sisi', 'bibi', 'titi', 'carla']
#
# print(list(map(lambda item: item.upper(), my_pets)))

# print(list(map(lambda num: num**2, [1,2,3])))
#
# a = [(0, 2), (5, 2), (9, 9), (10, -1)]
# a.sort(key=lambda x: x[1])
#
# print(a)
#
# my_list=[num for num in range (0,20)]
# my_list1=[2*num for num in range (0,20)]
# my_list2=[2*num for num in range (0,20) if num %2==0]
#
# print(my_list)
# print(my_list1)
# print(my_list2)

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#
#
# duplicates={dup for dup in  some_list if some_list.count(dup) >1 }
# print(list(duplicates))

# performance decorator.
# from time import time
# def performance(fn):
#   def wrapper(*args, **kwargs):
#     t1 = time()
#     result = fn(*args, **kwargs)
#     t2 = time()
#     print(f'took {t2-t1}')
#     return result
#   return wrapper
#
# @performance
# def long_time():
#     for i in range(10000):
#         i*5
#
# long_time()

# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
# user1 = {
#     'name': 'Sorna',
#     'valid': False #changing this will either run or not run the message_friends function.
# }
#
# def authenticated(fn):
#   # code here
#   def test(x):
#     if bool(x['valid']) == True:
#       fn(x)
#
#   return test
#
# @authenticated
# def message_friends(user):
#     print('message has been sent')
#
# message_friends(user1)

# from time import time
# def performance(fn):
#     def wrapper(*args, **kawrgs):
#         t1 = time()
#         result = fn(*args, **kawrgs)
#         t2 = time()
#         print(f'took {t2-t1} s')
#         return result
#     return wrapper
#
# @performance
# def long_time():
#     print('1')
#     for i in range(100000):
#         i*5
# @performance
# def long_time2():
#     print('2')
#     for i in list(range(100000)):
#         i*5
#
#
# long_time()
# long_time2()
#
# def special_for(iterable):
#   iterator = iter(iterable)
#   while True:
#     try:
#       iterator*5
#       next(iterator)
#     except StopIteration:
#       break
#
#
# class MyGen:
#   current = 0
#   def __init__(self, first, last):
#     self.first = first
#     self.last = last
#     MyGen.current = self.first #this line allows us to use the current number as the starting point for the iteration
#
#   def __iter__(self):
#     return self
#
#   def __next__(self):
#     if MyGen.current < self.last:
#       num = MyGen.current
#       MyGen.current += 1
#       return num
#     raise StopIteration
#
# gen = MyGen(1,100)
# for i in gen:
#     print(i)

# def fib(n):
#     i = 0
#     j = 1
#
#     for f in range(n):
#         yield i
#         sum= i+j
#         i=j
#         j=sum
#
#
# for x in fib(10):
#     print(x)

# #Write a program which will find all such numbers which are divisible by 7 but are
# # not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained
# # should be printed in a comma-separated sequence on a single line.
#
# for i in range(2000,3201):
#     if i%7== 0 and i%5!=0:
#         print(i,",", end="")
#


# Write a program which can compute the factorial of a given numbers.The results
# should be printed in a comma-separated sequence on a single line.Suppose the
# following input is supplied to the program: 8 Then, the output should be:40320
#
# start= int( input(('Input a number ')))
# i=1
# factorial=1
# while i<= start:
#     factorial= factorial*i
#     i+=1
#
# print(f'{start} Then, the output should be: {factorial}')

# With a given integral number n, write a program to generate a dictionary that
# contains (i, i x i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.Suppose the following input is
# supplied to the program: 8 Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#
# num= int(input("enter a number: "))
# my_list=[]
# my_squeares=[]
# for i in range (1,num+1):
#     my_list.append(i)
#     my_squeares.append(i*i)
#
# print ("Original key list is : " + str(my_list))
# print ("Original value list is : " + str(my_squeares))
#
# my_dict= {}
# for key in my_list:
#     for value in my_squeares:
#         my_dict[key] = value
#         my_squeares.remove(value)
#         break
#
# print ("Resultant dictionary is : " +  str(my_dict))


# Question:
#
#     Write a program which accepts a sequence of comma-separated numbers
# from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:

# values= input('enter your list of numbers ')
# lil = values.split(",")
# my_list=[(num) for num in lil ]
# my_tuple=((num) for num in lil)
#
# print(my_list)
# print(tuple(my_tuple))
#
# Question 5
# Question:
#
#     Define a class which has at least two methods:
#
#         getString: to get a string from console input
#         printString: to print the string in upper case.
#
#     Also please include simple test function to test the class methods.

# class Major:
#     def getString(self,stringg):
#         self.stringg= stringg
#
#     def printString(self):
#        print (self.stringg.upper())
#
#
#
# s1= Major()
# s1.getString(str(input('enter a string: ')))
# s1.printString()


#     Write a program that calculates and prints the value according to the given formula:
#
#     Q = Square root of [(2 _ C _ D)/H]
#
#     Following are the fixed values of C and H:
#
#     C is 50. H is 30.
#
#     D is the variable whose values should be input to your program in a comma-separated
#     sequence.For example Let us assume the following comma separated input sequence is given
#     to the program:
#
# 100,150,180
#
#     The output of the program should be:
#
# 18,22,24

#
# import math
# (c,h)= (50,30)
# string=input('give a list of numbers separated by comma: ')
#
# for item in string.split(','):
#
#     print(round(math.sqrt(2 * c * float(item)/h)),end=', ')

# Question:
#
#     _Write a program which takes 2 digits, X,Y as input and generates a
# 2-dimensional array. The element value in the i-th row and j-th column of the
# array should be i _ j.*
#
#     Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given
# to the program: 3,5
#
#     Then, the output of the program should be:
#
# [[0, 0, 0, 0, 0],
#  [0, 1, 2, 3, 4],
#  [0, 2, 4, 6, 8]]

# inn=input('input a number: ').split(',')
# i=int(inn[0])
# j=int(inn[1])
# list=[]
#
# for item in range(0,i):
#     sub_list = []
#     for tem in range(0,j):
#         sub_list.append(item*tem)
#     list.append(sub_list)
#
#
# print(list)

# import sys
#
# sys.argv

# Question 8
# Question:
#
#     Write a program that accepts a comma separated sequence of words as
# input and prints the words in a comma-separated sequence after sorting them alphabetically.
#
#     Suppose the following input is supplied to the program:
#
# without,hello,bag,world
#
#     Then, the output should be:
#
# bag,hello,without,world

# to_sort= 'without,hello,bag,world'.split(',')
# to_sort.sort()
# for i in    to_sort:
#     print(i,end=', ')
#
# Question 9
# Question:
#
#     Write a program that accepts sequence of lines as input and
# prints the lines after making all characters in the sentence capitalized.
#
#     Suppose the following input is supplied to the program:
#
# Hello world
# Practice makes perfect
#
#     Then, the output should be:
#
# HELLO WORLD
# PRACTICE MAKES PERFECT
#
# line=""
#
# while True:
#     new_line=(str(input('GIVE ME SOME ')))
#     if new_line:
#         line+=new_line.upper()+'\n'
#     else:
#         break
#
# print(line)
#
#
# Question 10
# Question
#
#     Write a program that accepts a sequence of whitespace separated
#  words as input and prints the words after removing all duplicate words
# and sorting them alphanumerically.
#
#     Suppose the following input is supplied to the program:
#
# hello world and practice makes perfect and hello world again
#
#     Then, the output should be:
#
# again and hello makes perfect practice world
#
# my_list=list(set('hello world and practice makes perfect and hello world again'.split(' ')))
# my_list.sort()
# print(' '.join(my_list))


# word = input().split()
#
# for i in word:
#     if word.count(i) > 1:    #count function returns total repeatation of an element that is send as argument
#         word.remove(i)     # removes exactly one element per call
#
# word.sort()
# print(" ".join(word))

#
# Question 11
# Question
#
#     Write a program which accepts a sequence of comma separated 4 digit
# binary numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
#
#     Example:
#
# 0100,0011,1010,1001
#
#     Then the output should be:
#
# 1010
#
#     Notes: Assume the data is input by console.

# innn=input('Input a list of binaries:' ).split(',')
# new_list=[]
# for item in innn:
#     if int(item , 2) %5==0:
#         new_list.append(item)
#     else:
#         pass
#
# for item in new_list:
#     print(item)

# Question 12
# Question:
#
#     Write a program, which will find all such numbers between 1000 and
# 3000 (both included) such that each digit of the number is an even number.The numbers
# obtained should be printed in a comma-separated sequence on a single line.
#
# Hints:
#
#     In case of input data being supplied to the question, it should be assumed to be a console input.
#


# list = []
# for numbers in range(1000,3001):
#     j = 0
#     i = 0
#
#
#     string_form = str(numbers)
#
#     while j<4:
#
#         if (int(string_form[j]) %2==0):
#             i+=1
#         else:
#             pass
#         j+=1
#
#     if i==4:
#         list.append(str(numbers))
#
# print(','.join(list))


# number=input('give me a number: ').split(',')
# list=[]
# for item in number:
#     if number.count(item)==1:
#         list.append(item)
#
#
# print(','.join(list))
#


# def hasArrayTwoCandidates(A, arr_size, sum):
#
#     new_list=sorted(A)
#     l = 0
#     r = arr_size - 1
#     list=[]
#
#     while l < r:
#         if (new_list[l] + new_list[r] == sum):
#             list.append(new_list[l])
#             list.append(new_list[r])
#             return 1
#         elif (new_list[l] + new_list[r] < sum):
#             l += 1
#         else:
#             r -= 1
#     return 0
#
#
#
# A = [1, 4, 45, 6, 10, -8]
# n = 16
# if (hasArrayTwoCandidates(A, len(A), n)):
#     print("Array has two elements with the given sum")
#
# else:
#     print("Array doesn't have two elements with the given sum")
#
# def PairedN(arr, arr_size, sum):
#     s = set()
#
#     for i in range(0, arr_size):
#         temp = sum - arr[i]
#         if (temp in s):
#             x = arr.index(temp)
#             y = arr.index(arr[i])
#             if x + y == sum:
#                 print(f"Pair with given sum {str(sum)} is ({str(arr[i])} at index {y} , {str(temp)}  at index {x})")
#         s.add(arr[i])
#
#
# A = [1, 6, 45, 4, 3, 8]
# n = 7
# PairedN(A, len(A), n)


# Question 13
# Question:
#
#     Write a program that accepts a sentence and calculate the number of letters and digits.
#
#     Suppose the following input is supplied to the program:
#
# hello world! 123
#
#     Then, the output should be:
#
# LETTERS 10
# DIGITS 3


#
# lst = [str(i) for i in input('give me a str: ')]
#
# letters=0
# nums=0
# for i in lst:
#     if ord(i) in range(48,58):
#         nums+=1
#     elif ord(i) in range  (65,91):
#         letters += 1
#     elif ord(i) in range (97, 123):
#             letters+=1
#     else:
#         print('input a right character')
# print(f'letters {letters}')
# print(f'numbers {nums}')

# word = input()
# letter, digit = 0,0
#
# for i in word:
#     if i.isalpha(): # returns True if alphabet
#         letter += 1
#     elif i.isnumeric(): # returns True if numeric
#         digit += 1
# print(f"LETTERS {letter}\n{digits}") # two different types of formating method is shown in both solution


# f= open('test.txt', 'a')
# f.write('This is my new text file')
# f.close()
#
# f= open('test.txt', 'r')
# print(f.read())

# import os
#
# if os.path.exists ('test.txt'):
#     os.remove('test.txt')


# #pip install translate
# with open('test.txt','w') as f:
#     f.write('my name is simpson')
# from translate import Translator
# translator= Translator(to_lang="zh")
# with open('test.txt','r') as f:
#     text=f.read()
#     translation = translator.translate(text)
#     print (translation)


# import re
#
#
# string= 'the apple tcame from this tree'
#
# a=re.search('this', string)
#
# print(a)
# print(a.span())
# print(a.start())
# print(a.end())
#
# pattern=re.compile(r'([a-zA-Z]).([a])')
# string='the apple came from this tree this'
# a=pattern.search(string)
# b=pattern.findall(string)
# c=pattern.fullmatch(string)
#
# print(a,b,c,a.group())


#
# import re
#
# pattern=re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# string='gawakgwak200@hotmail.com'
# a=pattern.search(string)
#
#
# print(a)

#
# # password with any amount of cahracters starting from 8
# # must contain $@%#
# # ends with a number
# import re
#
#
# pattern=re.compile(r"[a-zA-z@$%#]{8,}\d")
# string='gawakgwak2'
# a=pattern.search(string)
# check=pattern.fullmatch(string)
#
# print(check)

#
# from turtle import *
# color('green')
# bgcolor('black')
# speed(10)
# b=0
# while b<200:
#     left(b)
#     forward(b*3)
#     b+=1

# def addin(num):
#     num+=5
#     return num


# string=(str(i) for i  in input('input a bunch of words: '))
# ucase,lcase=0,0
# for i in string:
#     if ord(i) in range(65,91):
#         ucase+=1
#     if ord(i) in range(97, 123):
#         lcase+=1
#
# print(f'uppercase: {ucase}, lowercase {lcase}')
#
# word = input()
# upper,lower = 0,0
#
# for i in word:
#     if 'a'<=i and i<='z' :
#         lower+=1
#     if 'A'<=i and i<='Z':
#         upper+=1
#
# print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))

# word = input()
# upper,lower = 0,0
#
# for i in word:
#         lower+=i.islower()
#         upper+=i.isupper()
#
# print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))



# Question 15
# Question:
#
#     Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
#
#     Suppose the following input is supplied to the program:
#
# 9
#
#     Then, the output should be:
#
# 11106
# a=input('give me a number ')
# mlist=0
# stri=a
#
# for i in range(0,4):
#         mlist+=(int(stri))
#         stri+=a
#
# print(mlist)



# Question:
#
#     Use a list comprehension to square each odd number in a list. The list is input
# by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:
#
# 1,2,3,4,5,6,7,8,9
#
#     Then, the output should be:
#
# 1,9,25,49,81


# mt_list=[int(i) for i in input('list: ').split(',')]
#
# mylist1=[i*i for i in mt_list if  (i%2!=0)]
#
# print(mylist1)

# Question 17
# Question:
#
#     Write a program that computes the net amount of a bank account based
# a transaction log from console input. The transaction log format is shown as following:
#
# D 100
# W 200
#
#     D means deposit while W means withdrawal.
#
#     Suppose the following input is supplied to the program:
#
# D 300
# D 300
# W 200
# D 100
#
#     Then, the output should be:
#
# 500

#
# import random
#
# def ranndomize(guess,answer):
#
#         if guess==answer:
#                 print('you are a genius')
#                 return True
#         else:
#                 print('wrong')
# if __name__ == '__main__':
#         answer=random.randint(1,2)
#         guess=int(input('sdbdsd: '))
#
#         ranndomize(guess,answer)



# from PIL import Image,ImageFilter
#
# img =  Image.open('./astro.jpg')
# img.thumbnail((400,200))
# img.save('thumbnail.jpg')


import PyPDF2

with open('dummy.pdf', 'rb') as file:
    reader=PyPDF2.PdfFileReader(file)
    print(reader.numPages)


import PyPDF2

with open('dummy.pdf', 'rb') as file:
    reader=PyPDF2.PdfFileReader(file)
    print(reader.numPages)

