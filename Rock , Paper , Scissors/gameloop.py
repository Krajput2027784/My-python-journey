import random

print("🎮 Game: Rock, Paper, Scissors 🎮")

choose = ["rock", "paper", "scissors"]

while True:
    User = input("Enter your choice (rock/paper/scissors): ").lower()

    if User not in choose:
        print("❌ Invalid choice! Please enter rock, paper or scissors.")
        continue

    computer = random.choice(choose)

    print("Computer:", computer, "😎")
    print("User:", User, "👤")

    if User == computer:
        print("Draw 😣")

    elif (User == "paper" and computer == "rock") or \
         (User == "scissors" and computer == "paper") or \
         (User == "rock" and computer == "scissors"):
        print("You Win! 🤩")

    else:
        print("Computer Wins 🤭")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing! 🤝")
        break