

num1= float(input("Enter a number: "))
operation = input ("Enter operator(+ , - , * or /): ")
num2= float(input("Enter another number: "))

if operation == "+":
    print( num1 + num2 )

elif operation == "-":
    print( num1 - num2 )

elif operation == "*":
    print( num1 * num2 )

elif operation == "/":
    print( num1 / num2 )

else:
    print("ERROR!!!!(Invalid operator")