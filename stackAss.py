# import math
# stack=[79, 77,54,81,48,34,25,16]
# count=0

# for i in stack:
#     root = math.isqrt(i)
#     if root*root == i:
#         count=count+1
    
# print(count)   


#----------------------------------------------------------------------------------------------------------#

# def func(value,values):
#     var = 1
#     values[0] =44
# t=3
# v=[1,2,3]
# func(t,v)
# print(t,v[0])

#----------------------------------------------------------------------------------------------------------#

# def f(i,values =[]):
#     values.append(i)
#     print(values)
# f(1)
# f(2)
# f(3)

#----------------------------------------------------------------------------------------------------------# 
# str="Learning Python is very easy"
# n=len(str)
# i=0
# print("Forward Direction")
# while i<n: 
#     print(str[i],end='  ')
#     i+=1
# print()
# print("Backward Direction")
# i=-1
# while i>=-n:
#     print(str[i],end='  ')
#     i=i-1

#----------------------------------------------------------------------------------------------------------#
# input = "abcdfjgerj    abcdfjger"

# for i in input:
#     if i not in output:
#       print(i)
# print()      
        
#----------------------------------------------------------------------------------------------------------#

# v=['a','e','i','o','u']
# w=input("Enter the word where we will search the vowels:")
# found =[]
# for i in w:
#     if i in v:
#         if i not in found:
#             found.append(i)
# print('Found vowels:', found)
# print('unique vowels:', len(found),'from the given word',w)

#----------------------------------------------------------------------------------------------------------#

# x,y,z =map(int,input().split())
# mylist =[] 
# for i in range(x):
#     a =int(input())
#     mylist.append(a)
# for j in mylist:
#     if j>=y and j<=z:
#         print(j,end=' ')

#----------------------------------------------------------------------------------------------------------#

# #dateTime
# import datetime
# #datetime formatting
# date=datetime.datetime.now()
# print("It's now :{:%d/%m/%Y %H:%M:%S}".format(date))

#----------------------------------------------------------------------------------------------------------#

# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3]
# print(x==y)
# print(x==z)
# print(x!=z)

#----------------------------------------------------------------------------------------------------------#

# val =[2**i for i in range(1,6)]
# print(val)

#----------------------------------------------------------------------------------------------------------#

#dictionary comprehension
# squares={x:x*x for x in range(1,6)}
# print(squares)

# doubles={x:2*x for x in range(1,6)}
# print(doubles)

# a,b=[int(x) for x in input("Enter 2 numbers:").split()]
# print("Product is :" , a*b)


# a,b,c= [float(x) for x in input("Enter 3 numbers:").split(' , ')]
# print("Sum is :" , a+b+c)


#----------------------------------------------------------------------------------------------------------#
# #you can use else with for
# #using else block
# mycart=[10,20,800,60,70]
# for item in mycart:
#     if item>400:
#         print("This is not in my budget")
#         continue
#     print(item)
# else:
#     print("You have Purchased Everything")

#----------------------------------------------------------------------------------------------------------#
# while True:
#   username=input("Enter Username:")
#   password=input("Enter Password:")
#   if (username== 'admin ' and password=='admin'):
#     print("Login Successfully")
#     break
#   else:
#     continue
    

#----------------------------------------------------------------------------------------------------------#
#Tower Of Hanoi

import time
class Tower:
    def __init__(self):
        print("WELCOME TO TOWER OH HANOI GAME")
        print()
        print("Given Problem  A=[3,2,1]    B=[]    C[]  ")
        print()
        print("Expected Output A=[]   B=[]  C=[3,2,1]")
        self.A =[]
        self.B =[]
        self.C =[]
    def tower(self,item):
        self.A.append(item)
        time.sleep(3)
        print("A=",self.A)
        print("Items in Tower A\n")
    def pass1(self):
        self.temp =self.A.pop(2)
        self.C.append(self.temp)
        time.sleep(3)
        print ("A=",self.A     , "  ", "B=",self.B   , "  ","C=", self.C )
        print("pass one completed=============")
    
    def pass2(self):
        self.temp =self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A     , "  ", "B=",self.B   , "  ","C=", self.C )
        print("pass two completed=============")

    def pass3(self):
        self.temp =self.C.push(0)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A     , "  ", "B=",self.B   , "  ","C=", self.C )
        print("pass three completed=============")
    
    def pass4(self):
        self.temp =self.A.pop(2)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A     , "  ", "B=",self.B   , "  ","C=", self.C )
        print("pass four completed=============")
    
    def pass5(self):
        self.temp =self.B.pop(2)
        self.A.append(self.temp)
        time.sleep(3)
        print("A=",self.A     , "  ", "B=",self.B   , "  ","C=", self.C )
        print("pass five completed=============")
    
    def pass6(self):
        self.temp =self.B.pop(2)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A     , "  ", "B=",self.B   , "  ","C=", self.C )
        print("pass six completed=============")

    def pass7(self):
        self.temp =self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A     , "  ", "B=",self.B   , "  ","C=", self.C )
        print("pass seven completed=============")

obj =Tower()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()