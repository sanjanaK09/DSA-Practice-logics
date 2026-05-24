# import re #module for performing regular expression 
# count =0 #count the number of matching found
# pattern =re.compile("function")


# matcher =pattern.finditer("A function in python is defined by a def statement python . The general syntax looks like this:def function name statements,i.e. the function body .The parameter python list consists of none or more parameters:")
# for i in matcher :
#     count+=1
#     print(i.start(),".....",i.end(),".....",i.group())
# print("The number of occurrences:",count)


# import re
# count =0
# matcher = re.finditer("Hi","HiHiHiHiHi")

# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurrences:",count)

# import re 
# obj = input("enter any character")
# objmatch = re.finditer(obj,"a7b @k9z")
# for match in objmatch:
#     print(match.start(),"...",match.end(),"...",match.group())


# import re
# a = input("enter string to perform match operation :")
# mtch = re.match(a,"python is very important language")
# print(mtch)
# if mtch != None:
#     print("match found at beginning level")
#     print(mtch.start()," ",mtch.end())
# else:
#     print("there is no matching at beginning level")


# import re
# a = input("enter string to perform match operation :")
# mtch = re.match(a,"pythonisvery")
# print(mtch)
# if mtch != None:
#     print("match found")
#     print(mtch.start()," ",mtch.end())
# else:
#     print("Full match is not found")


# import re
# s = input("enter mail id:")
# m = re.fullmatch("\w[a-zA-Z0-9_.]*@rbunagpur[.]in",s)
# if m != None:
#     print("Valid Email Id")
# else:
#     print("Invalid Email Id")
#-----------------------------------------------
# import re
# s = input("enter mail id:")
# m = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
# if m != None:
#     print("Valid Email Id")
# else:
#     print("Invalid Email Id")
    
    
# import re
# mo = input("Enter mobile number")
# obj = re.fullmatch("[0-9]\d{9}",mo) 
# if obj!=None:
#     print("Valid mobile number")
# else:
#     print("Invalid mobile number") 
    
    
    
# import re
# a = input("enter string to perform match operation :")
# mtch = re.search(a,"python sss dynamic lannn")
# print(mtch)
# if mtch != None:
#     print("match found")
#     print(mtch.start()," ",mtch.end()," ",mtch.group())
# else:
#     print("there is no matching anywhere")


# import re
# mtch = re.findall('[A-Z]',"abch3hdh5bk7ZQ$&*")
# print(mtch)



# import re
# obj = re.sub('[a-z]',"*","abc HGFH 235")
# print(obj)

# import re
# obj = re.subn('[0-7]','@','ab3gd6sj17')
# print(obj)
# print("string is =",obj[0])
# print("number of replacement is =",obj[1])

