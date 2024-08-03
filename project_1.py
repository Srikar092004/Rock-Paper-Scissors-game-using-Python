import random
comp=random.choice([1,2,3]) #Computer chooses random number between 1,2 and 3
user=input("Rock, Paper, Sessors: ") #user chooses a number between r,p or s 
dict1={"r":1,"p":2,"s":3} #coverts user input to number
dict2={1:"Rock",2:"Paper",3:"Sessor"} #1=Rock, 2=Paper, 3=Sessor
usernum=dict1[user.lower()] #Converted usernumber stored 
print(f"You Chose {dict2[usernum]}\nComputer chose {dict2[comp]}") #Displaying the choices of user and computer
if(comp==usernum): #Tie Condition
    print("Tie !")
else: #Win or Lose Condtions
    if(comp==1 and usernum==2):
        print("You Win !")
    elif(comp==1 and usernum==3):
        print("You Lose !")
    elif(comp==2 and usernum==1):
        print("You Lose !")
    elif(comp==2 and usernum==3):
        print("you Win !")
    elif(comp==3 and usernum==1):
        print("You Win !")
    elif(comp==3 and usernum==2):
        print("You Lose !")
    else:
        print("Something Wrong")