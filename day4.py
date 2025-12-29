is_door_open = True
timer = 5 # seconds
print("Door now open!")
while timer >= 0:
    print(f'Timer in seconds {timer} s')
    timer = timer - 1

print("Door now closed!")

num = int(input("Enter a number: "))
num1 = int(input("Enter another number: "))
print (f"The sum is {num1+num}" )
com =input("Do you want to continue?(yes/no): ")

while com.strip().lower() == "yes" :
    num2 = int(input("Enter a number: "))
    num3 = int(input("Enter another number: "))
    print(f"The sum is {num2 + num3}")
    com = bool(input("Do you want to continue?"))
