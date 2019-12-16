## Basic Data Types
a = 10 #int
b = 5.2 #float
c = 'hello' #string
d = False #boolean
#print(a, b, c, d)

## Arrays
e = [5, a, b, 'abc'] #list
#print(e)
f = (1, c, True) #tuple
#print(f)
x, y, z = f #unpacking
#print(x)
#print(y)
#print(z)
g = {'A':123, 'B':2.5} #dictionary
#print(g)

#indexing
#print(f[6])
#print(g['B'])
#slicing
#print(e[-3:])

#control flow
#print(a)
#if a == 5:  # if statement
#    print('A is equal to five')
#    print('abc')
#    print('!!')
#elif a == 10:
#    print('Do something')
#else:
#    print('A is not five')
#print('done')

# while loop
#i = 0
#while i < 5:
#    print(i, 'Sarun')
#    i = i + 1

## for loop
#for i in range(5):
#    print(i, 'Sarun')
#
#print(e)
#for i in e:
#    print(i, 'e')

# 1. create function
#def f1():
#    print('Hello')
#    for j in range(3):
#        print('ZZZ')
#    print('Bye')
## 2. call function  
#for i in range(3):
#    f1()

# 1. load the library
import os
import datetime
# 2. call the function
print(datetime.datetime.now())













