# def linearSearch(array, target):
#     for i in range(0,len(array)):
#         if array[i] == target:
#             return i
#     return -1
# array = [1,2,3,4,8,7,9]
# target = 7 #search the target value i.e 7
# result=linearSearch(array , target)
# if result == -1:
#     print("target value not found")
# else:
#     print("Element found at index",result)






#Removing spaces from the string :
#1. rstrip()====>to remove spaces at right hand side
#2. lstrip()====>to remove spaces st the left hand side 
#3. strip()=====> to remove spaces both sides
city=input("enter your city name:")
scity=city.strip()
if scity == 'hyderabad':
    print("hello hydrabadi..Adab")
elif scity == 'Cehnnai':
    print("Hello Madrasi...Vanakkam")
elif scity == "Bengalore":
    print("Hello Kannadiga...Shubhodaya")
else:
    print("Your entered city is invalid")