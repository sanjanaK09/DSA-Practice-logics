# mydict = {
# 101:"prashant",
# 102:"ashish",
# "103": "mohini",##string datatype
# "104": "trivani",##string datatype
# 101:"ashish",
# 104:"ashish"}##integer data type

# print(mydict)

# #with the help of key we have to pritnt the values 
# # a = mydict[102]
# # print(a)

# # mydict[102] = "peter"
# # print(mydict)

# # #only print key x=0,1
# # for x in mydict:
# #     print(x)

# # ##printing values
# # for x in mydict.values():
# #     print(x)
    
# # ##printing key and values both 
# # for x,y in mydict.items():
# #     print(x,y)

# # ##adding a new key value pair
# # mydict["mobile_no"]=2237459277
# # print(mydict)

# # ##used to pop(delete) key item from the dict list 
# # mydict.pop(101)
# # print(mydict)


# a = {(1,2):1,(2,3):2,(4,5):3} ##(4,5)-->considered as a key
# print(a)
# print(a[4,5])


# a ={'a':1,'b':2,'c':3}
# print(a['a','b'])
##KeyError: ('a', 'b')


# arr = {}
# arr[1] =1
# arr['1'] = 2
# arr[1]+= 1
# print(arr)
# sum = 0
# for k in arr:
#     sum += arr[k]
# print(sum)

# ##{1: 2, '1': 2}
# #4


# my_dict ={}
# my_dict[1] =1
# my_dict['1'] =2
# my_dict[1.0] =4
# print(my_dict)
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
###{1: 4, '1': 2}
#6


# my_dict ={}
# my_dict[(1,2,4)] =8
# my_dict[(4,2,1)] =10
# my_dict[(1,2)] =12
# print(my_dict)
# ##{(1, 2, 4): 8, (4, 2, 1): 10, (1, 2): 12}
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
# print(my_dict)
# ##30
# ##{(1, 2, 4): 8, (4, 2, 1): 10, (1, 2): 12}


# box = {}
# jars = {}
# creates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# creates['box'] = box
# creates['jars'] = jars
# print(len(creates[box]))
# ##TypeError: unhashable type: 'dict'


# dict = {'c':97,'a':96,'b':98}
# for _ in sorted(dict):  ##sorts on the basis of keys
#     print (dict[_])


# rec = {"Name":"Python","Age":"20"}
# r = rec.copy()
# print(id(r) == id(rec))
# print(id(r))
# print(id(rec))
# ##False
# ##4375768000
# ##4375767808

# rec = {"name":"python"}
# id1= id(rec)
# print(id(rec))
# del rec
# rec = {"name":"python"}
# id2 =id(rec)
# print(id(rec))
# print(id1 == id2)
# ##true



###max values in the dictiopnary
# dict= {"A":50,"B": 30,"C": 70}
# for i in dict :
#     if dict[i] ==max(dict.values()):
#         print(i)
##OUTPUT-->C

###min values in the dictiopnary
# dict= {"A":50,"B": 30,"C": 70}
# for i in dict :
#     if dict[i] ==min(dict.values()):
#         print(i)
# ##OUTPUT-->B

# list=[1,2,2,3,4,3,5]
# dict={}
# for i in list:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# for key, value in dict.items():
#     print("key":"value")

###REVERSE oF number
# num= 123 #321
# a=num % 10 #a=3
# num =num //10 #num=12
# b = num % 10 #b=2
# c= num //10#c=1
# rev = a*100 + b*10 + c*1
# print(rev)


# num="123456"
# rev_number= num[::-1]
# print(rev_number)

# num= 123456
# a=num % 10 #6
# num =num //10
# b = num % 10
# num = num //10
# c= num %10
# num =num //10
# d= num %10
# num =num //10
# e= num %10
# f= num //10

# rev = a*100000 + b*10000 + c*1000 + d*100 + e*10 + f*1
# print(rev)



# Amount = int(input("Please enter amount for withdraw:"))
# print("100 notes=",Amount//100)
# print("50 notes=",(Amount%100)//50)
# print("20 notes=",((Amount%100)%50)//20)
# print("10 notes=",(((Amount%100)%50)%20)//10)
# print("5 notes=",((((Amount%100)%50)%20)%10)//5)
# print("2 coin=",(((((Amount%100)%50)%20)%10)%5)//2)
# print("1 coin=",((((((Amount%100)%50)%20)%10)%5)%2)//1)


##count num of occurence 
# arr = [1,1,0,1,1,1,0,0,1,1,1,1]
# max_count=0
# current_count=0
# for i in arr:
#     if i == 1:
#         current_count +=1
#         max_count = max(max_count,current_count)
#     else:
#         current_count = 0
# print(max_count)
     
    

# ##while loop
# i = 1
# while i<=5: #i=1
#     print(i)
#     i+=1



# ##count sub string
# str="abababab"
# list="ab"
# count= str.count(list)
# print(count)

# ##type 2 of counting string 
# Str = "abababab"
# Str1 = "ab"
# count = 0
# for i in range(len(Str) - len(Str1) + 1):
#     if Str[i:i+len(Str1)] == Str1:
#         count += 1
# print(count)