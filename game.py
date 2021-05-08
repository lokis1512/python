import random 
print(" enter a num between 1 to 10 ")

choice = 0

while (choice<7):
    crt_ans= random.randrange(1,11)
    username = int(input("enter a num : "))
    if username == crt_ans:
        print(" you won ")
        break;
    else:
        choice += 1
        print("you have chance")
else:        
    print("better luck next time")