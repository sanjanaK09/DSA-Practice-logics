# phy= int(input("Enter marks of phy :"))
# chem= int(input("Enter marks of chem :"))
# math= int(input("Enter marks of math :"))
# total= phy+chem+math
# percentage=total/3.0
# print("Total =",total)
# print("Percentage =",percentage)
# if phy >=40 and chem >=40 and math >=40:
#     print("Pass")
# else:
#     print("Fail")
# gender = input("Enter your gender M/F :")
# if percentage >=65 and gender =="M":
#     print("Eligible for placement")
# else:
#     print("Not Eligible")

# for i in range(1,5):
#     if i ==3:
#         break

#zip() we can take multiple range function inside zip()
# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i==3 and j==3:
#         continue
#     print(i," ",j)
    
# for i in range(1,6):
#     if i==3:
#         continue
#     for j in range(5,0,-1):
#         if j==3:
#             continue
#         print(i," ",j)

for i in range(1, 6):
    j = 6-i
    if i == 3 and j == 3:
            continue
    print(i, " ", j)
