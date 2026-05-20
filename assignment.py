# # ##1st way(not complete)
# # def bubbleSort(array):
# #     for i in range(len(array)-1):
# #         for j in range(len(array)-i-1):
# #             if array[j] > array[j+1]:
# #                 temp = array[j]
# #                 array[j] = array[j+1]
# #                 array[j+1] = temp
# #             print(array)
# # array=input("Enter the array elements seperated by space:")
# # count=0
# # for i in array:
# #     for j in array:
# #         str='578378923'


##2nd way
mylist = [5,7,8,3,7,8,9,2,3]
newlist = []
for i in range(len(mylist)):
    count =0
    key = mylist[i]
    j = i+1 
    while j<len(mylist):
        if key == mylist[j]:
            newlist.append(key)
        j = j+1
print(len(newlist))