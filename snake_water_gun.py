
import random
'''
-1 = water
1 = snake
0 = gun
'''
# computer = -1 
computer=random.choice([-1,1,0])
reversedict = {1: "Snake", -1: "water", 0: "gun"}
youstr = input("Enter your choice: ")
youdict = {"s":1,"w":-1,"g":0}
you = youdict[youstr]
print(f"you choose {reversedict[you]}\ncomputer choose {reversedict[computer]}")

if(computer == you):
    print("It's a draw")
else:
    if(computer == -1 and you ==1):
        print("you win!")
    elif(computer == -1 and you == 0):
        print("you lose!")
    elif(computer == 1 and you == -1):
        print("you win!")
    elif(computer == 1 and you == 0):
        print("you lose!")
    elif(computer == 0 and you == -1):
        print("you lose!")
    elif(computer == 0 and you == 1):
        print("you win!")
    else:
        print("something went wrong!")
        # it is the best example of nested if else


# it can also be done in simpler method in just 4 line code 
# if((computer-you) == -1 or (computer-you) == 2):
#     print("you lose!")
# else:
#     print("you win!")