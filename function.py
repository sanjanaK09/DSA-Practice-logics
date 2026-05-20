# difference between func and method function is defined outside class , method is defined inside class

# def hello(): #called funtion
#     print("hello world")
# hello() #calling funtion
# hello()


# def arithmetic():
#     a = int(input("Enter value of a:"))
#     b = int(input("Enter value of b:"))
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum, sub, div, mul       #it will return a tuple value ,values are static in tuple 
# # print(arithmetic()) #()parenthesis returns tuple value
# result = arithmetic()
# print("Arithmetic=",result)




## types of arguments we pass in a function
 ##--positional argument
 ##--keyword argument
 ##--default argument
 ##--variable length argument / variable number of arguments
 

# def arithmetic(a,b):
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum, sub, div, mul 
# #positional argument
# result = arithmetic(5,5)
# print("Arithmetic = ",result)

# ##keword argument
# def credentials(username,password): ##keword name and paramenter name must be same 
#     if username == password:
#         print("login succefully")
#     else:
#         print("Invalid credentials")

# credentials(username="admin", password="admin")


##default argument
# def cityname(city):
# def cityname(city="Pune"):
#     print(city)

# cityname("Nagpur")
# cityname("Mumbai")
# cityname()##give error



#  ##--variable length argument / variable number of arguments
# def cityname(*name):
#     print(name)

# cityname("Nagpur","delhi", "Mumbai","pune")


