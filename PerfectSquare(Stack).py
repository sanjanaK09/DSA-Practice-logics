# import math 
# stack = [79,77,54,81,48,34,25,16]
# count =0
# for i in stack:
#     root = math.isqrt(i)
#     if root*root == i:
#         count +=1
# print(count)


# ##
# def func(value, values):
#     var =1
#     values[0]=44
# t=3
# v=[1,2,3]
# func(t,v)
# print(t, v[0])
# ##OUTPUT:3 44

# def f(i, values=[]):
#     values.append(i)
#     print(values)
# f(1)
# f(2)
# f(3)
##OUTPUT- [1]
# [1, 2]
# [1, 2, 3]



import sys
class Queue:
    def __init__(self,size):
        self.myQueue =[]
        self.queueSize = size
    
    def isFull(self):
        if len(self.myQueue) == size:
            return True
        else:
            return False
    def enQueue(self,value):
        if self.isFull():
            print("Queue is Full")
        else:
            self.myQueue.append(value)
    
    
    
size = int(input("Enter the size of Queue:"))
obj = Queue(size)
print("Stack has created:")
while True:
    print("1.enqueue op:")
    print("2.display queue:")
    print("3.delete op:")
    print("4.peek op:")
    print("5.delete queue:")
    print("7.exit:")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        obj.enQueue()
    