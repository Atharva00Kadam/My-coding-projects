first_number = input("Welcome to Shloks calculator!"
                     "Enter your first number of operation: ")
second_number = input("Enter your second number: ")
Operation = input("Which operation would you like to perform?"
                  "\n / \n * \n + \n - \n Enter it here: ")
if Operation == "/":
    required_op1 = int(first_number) / int(second_number)
    print(required_op1)
elif Operation == "+":
    required_op2 = int(first_number) + int(second_number)
    print(required_op2)
elif Operation == "-":
    required_op3 = int(first_number) - int(second_number)
    print(required_op3)
elif Operation == "*":
    required_op4 = int(first_number) * int(second_number)
    print(required_op4)
else:
    print("Invalid operation")
    
