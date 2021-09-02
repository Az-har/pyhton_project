import random 
print("U most likely know the rules of the rock paper scissor\n So lets get started")
while True:
    print("Enter THE CHOICE \n 1.ROCK \n 2.PAPER \n 3.SCISSOR\n")
    choice=int(input("YOUR TURN ENTER HERE : "))
    while choice >3 or choice<1:
        print("BRUH ! Enter a Real Choice Within 3 ")
        exit()
    if choice== 1:
        a_name= 'rock'
    elif choice==2:
        a_name= 'paper'
    elif choice==3:
        a_name='scissor'
    print("UR CHOICE is "+ a_name)
    r= random.SystemRandom()
    comp =r.randint(1,3)
    if comp== 1:
            b_name= 'rock'
    elif comp==2:
            b_name= 'paper'
    elif comp==3:
            b_name='scissor'
    print("MY CHOICE IS "+b_name)
    
    if choice ==comp:
        print("Its a Tie")
    elif choice==1:
        if comp ==3:
           print("You Win")
        else:
            print("I Win")
    elif choice==2:
        if comp ==1:
           print("You Win")
        else:
            print("I Win")
    
    elif choice==3:
        if comp ==2:
           print("You Win")
        else:
            print("I Win")
    play_again =input("play again (y/n): ")
    if play_again.lower()!="y":
        break


print ("BRO it's lonely don't leave me!")


# import random
# print("U most likely know the rules of the rock paper scissor\n So lets get started")
  
# while True:
#     print("Enter THE CHOICE \n 1.ROCK \n 2.PAPER \n 3.SCISSOR\n")
#     a=int(input("YOUR TURN ENTER HERE : "))
#     if(a <3 or a>1):
#         print("ENTER A REAL CHOICE Within 3 ")


#     if(a==b):
#      print("draw")
#      ans = input("Wanna go An Another Round (Y/N)")
#      if ans == 'n' or ans == 'N':
#         break    


#     elif((a == 1 and b == 2) or
#       (a == 2 and b ==1 )):
#         print("paper wins ", end = "")
#         result = "paper"
          
#     elif((a == 1 and b == 3) or
#         (a == 3 and b == 1)):
#         print("Rock wins =>", end = "")
#         result = "Rock"
#     else:
#         print("scissor wins =>", end = "")
#         result = "scissor"
  
    
#     if result == a_name:
#         print(" U wins ")
#     else:
#         print(" I wins ")
          
#     print("Wanna go An Another Round (Y/N)")
#     ans = input()
  
#     if ans == 'n' or ans == 'N':
#         break


# print("so ur gonna run very well")














 