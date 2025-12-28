num1 = int(input("Enter a number : "))
num2 = int(input("Enter another number : "))
oper = str(input("Enter an operator : "))
if oper == "+":
    print(num1 + num2)
elif oper == "-":
    print(num1 - num2)
elif oper == "*":
    print(num1 * num2)
else:
    print(num1 / num2)