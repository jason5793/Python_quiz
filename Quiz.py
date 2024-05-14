import random
# Define your questions and options
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["1. Paris", "2. London", "3. Rome", "4. Berlin"],
        "answer": 1
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["1. Venus", "2. Mars", "3. Jupiter", "4. Saturn"],
        "answer": 2
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["1. H2O", "2. CO2", "3. NaCl", "4. O2"],
        "answer": 1
    }
]

# Shuffle the options for each question
for question in questions:
    random.shuffle(question["options"])

# Present the shuffled options to the user and take the answer
score = 0
for i, question in enumerate(questions, 1):
    print(f"\n{i}. {question['question']}")
    for option in question["options"]:
        print(option)
    user_answer = input("Enter your answer (number): ")
    
    # Validate the answer and provide feedback
    if user_answer.isdigit() and 1 <= int(user_answer) <= len(question["options"]):
        user_answer = int(user_answer)
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    else:
        print("Invalid input. Please enter a number corresponding to the options.")

# Display the final score
print(f"\nYour final score is {score} out of {len(questions)}.")
