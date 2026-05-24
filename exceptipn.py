# except ZeroDivisionError:
#     print("Cannot be devided by zero")
# except ValueError:
#     print("Enter only integer value:")
#     #Runtime error is also known as exception
# except:
#     print("ABC")

# except ZeroDivisionError:
#     print("Cannot be devided by zero")
# except ValueError:
#     print("Enter only integer value:")
# finally:
#     print("i am always excepted")#
    

# import logging
# logging.basicConfig(filename="newfile.txt",level=logging.DEBUG)
# try:
#     a = int (input("Enter first number:"))
#     b = int (input("Enter second number:"))
#     print(a/b)

# except(ZeroDivisionError,ValueError)as message:
#     print(message)
#     logging.exception(message)
# print("Logging level is set up.Check 'newfile.txt' for log details")

import csv
f=open("employee.csv",'a')
a = csv.writer(f)
# a.writerow(["EmpID","EmpName","EmpAge"])
empid= int(input("Enter your EmpId"))
empname= input("Enter your EmpName")
Age=int(input("Enter your Employee Age"))
# a.writerow(["EmpID","EmpName","EmpAge"])
a.writerow([empid,empname,Age])
print("file has created")
