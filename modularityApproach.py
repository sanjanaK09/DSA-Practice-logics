##modularity approach in function
import sys
def add():
    a = int(input("Enter values of A:"))
    b = int(input("Enter values of B:"))
    print(a+b)

def sub():
    a = int(input("Enter values of A:"))
    b = int(input("Enter values of B:"))
    print(a-b)

def div():
    a = int(input("Enter values of A:"))
    b = int(input("Enter values of B:"))
    print(a/b)
    
def mul():
    a = int(input("Enter values of A:"))
    b = int(input("Enter values of B:"))
    print(a*b)

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        add() #calling function 
    elif choice == 2:
        sub() #calling function
    elif choice == 3:
        div() #calling funtion
    elif choice == 4:
        mul() #calling function
    elif choice == 5:
        sys.exit()


##OUTPUT
    # 1. Addition
    # 2. Subtraction
    # 3. Division
    # 4. Multiplication
    # 5. Exit
    # Enter your choice:1
    # Enter values of A:2
    # Enter values of B:2
    # 4
    # 1. Addition
    # 2. Subtraction
    # 3. Division
    # 4. Multiplication
    # 5. Exit
    # Enter your choice:2
    # Enter values of A:2
    # Enter values of B:2
    # 0
    # 1. Addition
    # 2. Subtraction
    # 3. Division
    # 4. Multiplication
    # 5. Exit
    # Enter your choice:3
    # Enter values of A:2
    # Enter values of B:2
    # 1.0
    # 1. Addition
    # 2. Subtraction
    # 3. Division
    # 4. Multiplication
    # 5. Exit
    # Enter your choice:4
    # Enter values of A:2
    # Enter values of B:2
    # 4
    # 1. Addition
    # 2. Subtraction
    # 3. Division
    # 4. Multiplication
    # 5. Exit
    # Enter your choice:5 


