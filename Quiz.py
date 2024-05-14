import json
import random

# Load questions from the JSON file
with open("quiz_questions.json", "r") as file:
    questions = json.load(file)

# Shuffle the options for each question
for question in questions:
    random.shuffle(question["options"])

# Present the shuffled options to the user and take the answer
score = 0
total_questions = len(questions)
print("Welcome to the Quiz!")
print("You'll be presented with multiple-choice questions. Answer by typing the corresponding letter (a, b, c, or d).")
print("Let's get started!\n")

for i, question in enumerate(questions, 1):
    print(f"Question {i}/{total_questions}: {question['question']}")
    for idx, option in enumerate(question["options"], 1):
        print(f"{chr(96+idx)}. {option}")
    user_answer = input("Your answer: ").strip().lower()
    
    # Validate the answer and provide feedback
    if user_answer in ['a', 'b', 'c', 'd']:
        option_index = ord(user_answer) - 96
        if question["options"][option_index - 1] == question["answer"]:
            print("✅ Correct! Well done!")
            score += 1
        else:
            print("❌ Incorrect. Better luck next time!")
    else:
        print("Invalid input. Please enter a, b, c, or d.")

# Display the final score
print(f"\nQuiz completed! Your final score is {score} out of {total_questions}.")
