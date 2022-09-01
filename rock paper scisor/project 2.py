import random

print("winning Rules of Rock Paper Scissor Game as follows: \n"
      +"Rock vs Paper->paper wins \n"
      + "Rock vs Scissor->Rock wins \n"
      +"Paper vs Scissor->Scissor wins \n")

while True:
    print("Enter choice \n 1 for rock, \n 2 for Paper, and \n 3 for Scissor \n")

    choice = int(input("User Turn: "))

    while choice > 3 or choice < 1:
        choice = int(input("Enter Valid Input: "))

    if choice == 1:
        choice_name = 'Rock'
    if choice == 2:
        choice_name = 'Paper'
    if choice == 3:
        choice_name = 'Scissor'

    print("user choice is: " + choice_name)
    print("\nNow its computer turn.......")

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissor'

    print("Computer choice is: " + comp_choice_name)
    
    print(choice_name + " V/s " + comp_choice_name)

    #if choice == comp_choice:
          #print("Draw=> ", end = " ")
          #result = Draw

    if((choice == 1 and comp_choice ==2) or(choice == 2 and comp_choice ==1)):
        print("Paper wins => ", end = " ")
        result = "Paper"

    elif((choice == 1 and comp_choice ==3) or(choice == 3 and comp_choice ==1)):
          print("Rock wins => ", end = " ")
          result = "Rock"
    else:
        print("Scissor wins => ", end = " ")
        result = "Scissor"

    #if result == Draw:
        #print("<== Its a tie ==>")
    if result == choice_name:
        print("<== User Wins ==>")
    else:
        print("<== Computer Wins ==>")

    print("Do you want to play again? (Y/N)")
    ans = input().lower

    if ans == 'n':
        break

print("\nThanks for playing")
              
              
              
          
          
          
          
    


    


    
        
    
      

      

      

      

      
