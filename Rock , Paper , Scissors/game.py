print("🎮Game rock,paper and scissors🎮")
#let user select first from rock,paper,scissors
User = input("enter User's value(rock/paper/scissors):").lower()
print(User,"👌")#print the user's choice

import random #used to import choice of computer 
choose = ["rock" , "paper" , "scissors"]#choose in this list
computer = random.choice(choose)
print("Computer :",computer,"😎")#successfully print the computer's choice

if User == computer:#choices of user and computer are same 
   print("Draw","😣")#game draw between user and computer

elif (User == "paper" and computer == "rock")or\
 (User == "scissors" and computer == "paper" )or\
 (User == "rock" and computer == "scissors"):#conditions where user wins
    print("You win!","🤩")

else:
  print("Computer wins","🤭")#computer wins 