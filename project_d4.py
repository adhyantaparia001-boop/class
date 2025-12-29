for i in range(1,6) :
    if i == 1 :
        num = float(input("Enter price of first item "))
    if i == 2 :
        num1 = float(input("Enter price of second item "))
    if i == 3 :
        num2 = float(input("Enter price of third item "))
    if i == 4 :
        num3 = float(input("Enter price of fourth item "))
    if i == 5 :
        num4 = float(input("Enter price of fifth item "))
num5 = num1 + num2 + num3 + num4 +num
print(f"The cost is {num5} ")
print(f"After V.A.T the cost is {num5+num5*.13}")