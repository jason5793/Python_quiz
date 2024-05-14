import random

# Define your questions along with their correct answers and options
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "What is the tallest mountain in the world?",
        "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
        "answer": "Mount Everest"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Michelangelo"],
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "Which gas do plants absorb during photosynthesis?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "answer": "Carbon Dioxide"
    }
    # Add more questions here
]

# Function to shuffle the options for a question
def shuffle_options(options):
    shuffled_options = options[:]
    random.shuffle(shuffled_options)
    return shuffled_options

# Function to present the quiz and get user's answers
def take_quiz(questions):
    score = 0
    for i, question in enumerate(questions, 1):
        print(f"Question {i}: {question['question']}")
        shuffled_options = shuffle_options(question['options'])
        for idx, option in enumerate(shuffled_options, 1):
            print(f"{idx}. {option}")
        user_answer = input("Your answer: ").strip().title()  # Convert to title case
        if user_answer == question['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['answer']}\n")
    print(f"Your final score is: {score}/{len(questions)}")

# Run the quiz
take_quiz(questions)
