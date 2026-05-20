# # list1=[7,3,9,2,8]
# # list1.sort()
# # print(list1)
# # print(list1[-2])


# # a=[1,2,3,4,5,6,7,8,9]
# # a[::2]=10,20,30,40,50,60
# # print(a) //Valueerror

# # a=[1,2,3,4,5]
# # print(a[3:0:-1]) //4,3,2

# # arr = [[1,2,3,4],
# #        [4,5,6,7],
# #        [8,9,10,11],
# #        [12,13,14,15]]
# # for i in range(0,4):
# #     print(arr[i].pop()) ///4,7,11,15

# # arr =[1,2,3,4,5,6]
# # for i in range(1,6):
# #     arr[i-1] = arr[i]

# # for i in range(0,6):
# #     print(arr[i],end=" ")

# # fruit_list1 = ['apple','berry','cherry','papaya']
# # fruit_list2 = fruit_list1
# # fruit_list3 = fruit_list1[:]
# # fruit_list2[0]='Guava'
# # fruit_list3[1]='kiwi'

# # sum = 0
# # for ls in (fruit_list1, fruit_list2, fruit_list3):
# #     if ls[0]=='Guava':
# #         sum +=1
# #     if ls[1] =='kiwi':
# #         sum += 20
# #     print(sum)


# # arr1 = [1,2,3]
# # arr2 = [2,3,4]
# # arr3 = [3,4,5]
# # for i in arr1:
# #     if i in arr2 and i in arr3:
# #         print (i)

# mylist=[]
# arr= int(input("Enter array size"))
# for i in range(arr):
#     val = int(input("Enter array values :"))
#     mylist.append(val)
# print(mylist)

# sum=0
# for i in range(len(mylist)-1): #i=0
#     if i+1 in range(len(mylist)):
#         sum += abs(mylist[i]- mylist[i+1])
#     print(sum)



##wAP to reverse a string 

