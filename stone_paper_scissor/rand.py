import random


print("hello would you like to play a game")

while True:

    choice =int(input("enter a choice \n 1.rock \n 2.paper \n 3.scissor"))
    print("so you choose "+str(choice) )
   
    comp_choice = random.randint(1,4)
    print("the comp choice is " + comp_choice)

    if choice ==1:
       choice_name= 'rock' 
    elif choice ==2:
       choice_name= 'paper' 
    else :
        choice_name ="scissor"

    print("you have selected :" + str(choice_name))
       


    if choice==comp_choice:
        print("its a tie")
    elif choice==1 & comp_choice==2 :
        print("comp wins")
    elif choice==2 & comp_choice==1 :      
        print("player wins")
    elif choice==2 & comp_choice==3 :
        print("comp wins")
    elif choice==3 & comp_choice==2 :      
        print("player wins")
    elif choice==3 & comp_choice==1 :
        print("comp wins")
    else: #choice==1 & comp_choice==3 :      
        print("player wins")

    print("like to play agin (y/n)")
    cont = input()
    if cont == 'n':
        break
