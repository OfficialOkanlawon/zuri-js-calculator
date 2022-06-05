print("What operation do you want to perform?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

option = input("Select an option (1,2,3,4 0r 5) ")

if option in ("1", "2", "3", "4", '5'):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if option == '1':
        print("The addition is: " + str(num1 + num2))
    elif option == '2':
        print(num1-num2)
    elif option == '3':
        print(num1 * num2)
    elif option == '4':
        print(num1 / num2)
    elif option == '5':
        print(num1 % num2)
else:
    print("Invalid input")