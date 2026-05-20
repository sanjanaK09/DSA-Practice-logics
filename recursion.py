### when the main problem  can be divided into similar subproblem the recurtion can be used
### recursion uses stack memory
### recursion is neither space efficient nor time efficient 
# ##example:
# #factorial 
# def factorial(num):
#     if num <=1:
#         return 1
#     return num*factorial(num-1)
# print(factorial(4))

# #4*factorial(3)
# #3*factorial(2)
# #2*factorial(1)
# #4*3*2*1=24

# ##example
# #capoitalizeFirst
# def capitalizeFirst(arr):
#     result = []
#     if len(arr) == 0:
#         return result
    
#     result.append(arr[0][0].upper() + arr[0][1:])
#     return result + capitalizeFirst(arr[1:])
# print(capitalizeFirst(['car','taco','banana']))


##power of no
# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     return base *power(base,exponent-1)

# print(power(2,0))
# print(power(2,2))
# print(power(2,4))

# ##product of array solution

# def productOfArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0] * productOfArray(arr[1:])

# print(productOfArray([1,2,3]))
# print(productOfArray([1,2,3,10]))



# ##reverse a string using recursion
# def reverse(string):
#     if len(string) <= 1:
#         return string
#     return string[len(string)-1 ]+reverse(string[0:len(string)-1])

# print(reverse('python'))
# print(reverse('appmillers'))
# print(reverse('p'))


# ##recursiveRange solution
# def recursiveRange(num):
#     if num <=0:
#         return 0
#     return num + recursiveRange(num -1)
# print(recursiveRange(6))


# #palindrome 
# def isPalindrome(str):
#     if len(str) == 0:
#         return True
#     if str[0] != str[len(str)-1]:
#         return False
#     return isPalindrome(str[1:-1])
# print(isPalindrome('awesome'))
# print(isPalindrome('amanaplanacanalpanama'))
# print(isPalindrome('tacocat'))


# ##someRecursive Solution
# def someRecursive(arr,cb):
#     if len(arr) == 0:
#         return False
#     if not(cb(arr[0])):
#         return someRecursive(arr[1:],cb)
#     return True
# def isOdd(num):
#     if num%2 == 0:
#         return True
#     else:
#         return False
    
# print(someRecursive([1,2,3,4], isOdd))
# print(someRecursive([4,6,8,9], isOdd))
# print(someRecursive([4,6,8],isOdd))
# print(someRecursive([1,3,5,9],isOdd))





