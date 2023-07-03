num1 = float(input("Enter first number"))
op = input("choose an operator")
num2 = float(input("Enter second number"))
if op == "+":
    result = num1 + num2
    print(result)
elif op == "-":
    result = num1 - num2
    print(result)
elif op == "*":
    result = num1 * num2
    print(result)
elif op == "/":
    result = num1 / num2
    print(result)
elif op == "^":
    result = num1 ** num2
    print(result)
else:
    print("Invalid input")
