num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter operator: ")
if op == "+":
    res = num1 + num2
    print(res)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("Invalid Input")