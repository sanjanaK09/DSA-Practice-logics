# fruit ={}
# def addone(index):
#     if index in fruit :
#         fruit[index]  +=1
#     else:
#         fruit[index] =1
#     print(fruit)
# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))


#Write a program to accept stu name and marks from the keyboard and creates a dictionary. Also display student marks by taking student name
myDic=[]
class Student:
    def __init__(self):
        self.myDic ={}

    def student(self,name,marks):
        self.myDic[name]=marks
   
    def display(self,name):
      if name in self.myDic:
        print("Marks:",self.myDic[name])
      else:
        print("Student not found")

obj = Student()
name = input("Enter Student name:")
marks= input("Enter Student marks:")          
obj.student(name,marks)

search_name =input("Enter name to search:")
obj.display(search_name)