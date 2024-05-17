import json
import random
import threading
import time

def timer_expired():
    print("\nTime's up!")
    global time_up
    time_up = True

# Load questions from the JSON file
with open("quiz_questions.json", "r") as file:
    questions = json.load(file)

print("Welcome to the Quiz!")
print("You'll be presented with multiple-choice questions. Answer by typing the corresponding letter (a, b, c, or d).")
print("Let's get started!\n")

# Shuffle the options for each question
for question in questions:
    random.shuffle(question["options"])

score = 0
for i, question in enumerate(questions, 1):
    while True:
        print(f"\n{i}. {question['question']}")
        for option in question["options"]:
            print(option)
        
        time_up = False
        timer = threading.Timer(50.0, timer_expired)
        timer.start()

        user_answer = input("Enter your answer (a, b, c, d): ").strip().lower()
        
        timer.cancel()  # Cancel the timer if the user answers in time
        
        if time_up:
            print("You didn't answer in time.")
            break

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
