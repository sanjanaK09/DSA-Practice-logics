# name = "prashantjha" #string
# print(name[0])#p
# print(name[1])#r
# print(name[-1])#a
# #print(name[15])
# print(name[0:5]) #end -1, 5-1=4 prash
# print(name[1:]) #rashantjha
# print(name[:5])#5-1=4 prash
# print(name[:]) #prashantjha
# print(name[1:8:2]) #'''8-1=7 rsat
# print(name[::-1]) #reverse of string



# s = "Python are High level programing Language"
# print(s.lower())# python are high level programing language
# print(s.upper())# PYTHON ARE HIGH LEVEL PROGRAMING LANGUAGE
# print(s.swapcase())# pYTHON ARE hIGH LEVEL PROGRAMING lANGUAGE
# print(s.title())# Python Are High Level Programing Language
# print(s.capitalize())# Python are high level programing language



# name = "prashant"
# sal = 5000
# age = 28
# print("{} sal is {} age is {}".format(name,sal,age))
# print("{0} sal is {1} age is {2}".format(name,sal,age))
# print("{x} sal is {y} age is {z}".format(x=name,y=sal,z=age))


# name = "prashant"
# for i in name: #i=0:p----i=1:r-----i=2:a------
#     print(i)

# name =input("Enter name:")
# newname=""
# for i in name: 
#     if i not in newname:
#         newname += i
# print(newname)


# name ="prashant"
# newname=""
# N = len(name)
# for i in range(N-1,-1,-1): 
#     if i not in newname:
#         newname += name[i]
# print(newname)
 
 
# name = "racecar"
# print(name)
# print(name[::-1])
# if name == name[::-1]:
#     print("palindrome")
# else:
#     print("not palindrom")
    

# vowels = ['a','e','i','o','u']
# name = "HELLO"
# con=0
# vow=0
# for i in name:
#     if i in vowels:
#         vow +=1
#     else:
#         con +=1
# print("consonent=",con)
# print("vowels:",vow)

##count no of words in string 
# str=" This is the end "
# word =0
# space=0
# for i in str:
#     if i is None:
#         word +=1
#     else:
#         space +=1
# print(word)
# print(space)


# str=" This is the end "
# word =0
# space=0
# for i in str:
#     if i == " ":
#      space +=1
#     word = space-1
# print(word)
# print(space)

# str =input("enter the msg here:")
# char=0
# space=0
# spChar=['!','@','#','$','%','^','&','*','(',')','<','>','?','/',';','|']
# for i in str:
#     if i == " ":
#         space +=1
#     elif i != spChar:
#         char +=1
#     else:
#         spChar
# print(char)
# print(spChar)
# print(space)


# str="this is a test"
# print(str.title())


# str= input("Enter string :")
# print(str.isalnum())
# print(str.isalpha())
# print(str.isdigit())
# print(str.islower())
# print(str.islower())
# print(str.isupper())
# print(str.istitle())
# print(str.istitle())
# print(str.isspace())
# print("Hello".startswith("He"))
# print("Hello".endswith("lo"))


# print("Sanjanar".find("r"))
# print("Prashant".index("r"))
# print("prashant jha".count("a"))


##Nested loop
# print("1"," ","1"," ","1")
# print("2"," ","2"," ","2")
# print("3"," ","3"," ","3")

# #i=1 , j=1,(i,j=1,1)
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end =" ")
#     print()

# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()
    



# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print("*",end=" ")
#     print()




# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+j),end=" ")
#     print()
    
    
###Delay time 
# import time
# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     print(" "*(n-1),end=" ")
#     for j in range(1, i+1):
#         time.sleep(3)
#         print("*",end= " ")
#     print()


str1=[1,2,3,4]
str2= []



