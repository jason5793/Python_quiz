import json
import random
# Load questions from the JSON file
with open("quiz_questions.json", "r") as file:
    questions = json.load(file)
print("Welcome to the Quiz!")
print("You'll be presented with multiple-choice questions. Answer by typing the corresponding letter (a, b, c, or d).")
print("Let's get started!\n")

# Shuffle the options for each question
for question in questions:
    random.shuffle(question["options"])

# Present the shuffled options to the user and take the answer
score = 0
for i, question in enumerate(questions, 1):
    while True:
        print(f"\n{i}. {question['question']}")
        for option in question["options"]:
            print(option)
        user_answer = input("Enter your answer (a, b, c, d): ").strip().lower()
        
        # Validate the answer and provide feedback
        if user_answer in ['a', 'b', 'c', 'd']:
            if user_answer == question["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
            break  # Break out of the loop if the input is valid
        else:
            print("Invalid input. Please enter a, b, c, or d. Try again.")

# Display the final score
print(f"\nYour final score is {score} out of {len(questions)}.")
