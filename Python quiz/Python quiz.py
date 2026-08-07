print("===== PYTHON QUIZ =====")

questions = [
    ("Which language are we learning?", "python"),
    ("What is the output of 2 + 3?", "5"),
    ("Which keyword is used for a loop?", "for"),
    ("Which data type uses []?", "list"),
    ("Which data type uses ()?", "tuple")
]

score = 0

for question, answer in questions:
    print("\n" + question)
    user_answer = input("Your answer: ").lower()

    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\n===== RESULT =====")
print("Correct Answers:", score)
print("Total Questions:", len(questions))
print("Score:", score, "/", len(questions))

if score == len(questions):
    print("Excellent! 🎉")
elif score >= 3:
    print("Good Job! 👍")
else:
    print("Keep Practicing! 💪")