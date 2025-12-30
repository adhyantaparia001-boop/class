# info[10,20,30]
# i = 0
# while i < len(info):
#     print(info[i])
#     i+=1

list1 = []
leng = len(list1)
while leng < 5:
    leng += 1
    price_individual = int(input(f'Enter price for item {leng}: '))
    list1.append(price_individual)
total = 0
index = 0
while index < leng :
    total += list1[index]
    index += 1
print(f"Total cost is {total}")
print(f'Total with V.A.T is {total + (total*0.13)}')

