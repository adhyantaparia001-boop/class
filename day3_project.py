Age = int(input(" Enter your age :"  ))
Locat = str(input("Enter your location (note location can only be Kathmandu,Biratnagar,Pokhara) : "))
if Age >= 18 :
    if Locat.lower().strip() == "kathmandu" :
        print("You are eligible to vote")
        print("You have to go to Anamnagar to vote")
    if  Locat.lower().strip() == "biratnagar" :
        print("You are eligible to vote")
        print("You have to go to the Yellow Bridge to vote")
    if Locat.lower().strip() == "pokhara" :
        print("You are eligible to vote")
        print("You have to go to the Dam to vote")
    else:
        if Locat.lower().strip() != "kathmandu""biratnagar""pokhara":
            print("Input invalid")

elif Age < 18 :
    print("You are  not eligible to vote")
    if Locat.lower().strip() != "kathmandu""biratnagar""pokhara":
        print("Input invalid")