
num1 = float(input("Enter First Number: "))

operator = input("Enter Operator (+,-,*,/): ")

num2 = float(input("Enter Second Number: "))

if operator == '+':
    result = num1 + num2
    print(num1, "+", num2, "=", result)

elif operator == '-':
    result = num1 - num2
    print(num1, "-", num2, "=", result)

elif operator == '*':
    result = num1 * num2
    print(num1, "*", num2, "=", result)

elif operator == '/':
    result = num1 / num2
    print(num1, "/", num2, "=", result)

else:
    print("Invalid Operator")