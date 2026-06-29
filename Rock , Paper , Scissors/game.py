User = input("enter User's value(rock/paper/scissors):").lower()
print(User)

import random 
choose = ["rock" , "paper" , "scissors"]
computer = random.choice(choose)
print("Computer :",computer)

if User == computer:
   print("Draw")

elif (User == "paper" and computer == "rock")or\
 (User == "scissors" and computer == "paper" )or\
 (User == "rock" and computer == "scissors"):
    print("You win!")

elif User not in computer:
  print("invalid input")

else:
  print("winner")