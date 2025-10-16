import random

computer = random.choice([-1, 1, 0])
youstr = input("Enter your choice: ")
youDic = {"s": 1, "w": -1, "g": 0}
reverseDic= {1: "Snake", -1: "Water", 0: "Gun"}

you = youDic[youstr]

print(f"You chose {reverseDic[you]}\nComputer chose {reverseDic[computer]}")

if(computer == you):
    print("Its a Draw")

else:
    if(computer ==-1 and you ==1):
        print("You Win!")

    elif(computer ==-1 and you ==0):
        print("You Lose!")

    elif(computer ==1 and you ==-1):
        print("You Lose!")

    elif(computer ==0 and you ==-1):
        print("You Win!") 

    elif(computer ==0 and you ==1):
        print("You Lose!")

    elif(computer ==1 and you ==0):
        print("You Win!")
    

    else:
        print("Something went wrong!")                   