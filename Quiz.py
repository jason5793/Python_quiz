questions = [
    "How many elements are there in the periodic table?",
    "When did India gain independence?",
    "What is the largest river in India?",
    "Which of the following is the highest mountain?",
    "Who is the creator of the Python programming language?",
    "What is the capital of India?"
]

options = [
    ("A. 118", "B. 120", "C. 130", "D. 140"),
    ("A. 1947", "B. 1950", "C. 1945", "D. 1946"),
    ("A. Indus River", "B. Kaveri", "C. Yamuna", "D. The Ganges River"),
    ("A. K2 (Mount Godwin Austen)", "B. Mount Everest", "C. Kangchenjunga", "D. Cho Oyu"),
    ("A. Graydon Hoare", "B. Dennis Ritchie", "C. James Gosling", "D. Guido van Rossum"),
    ("A. Berlin", "B. New Delhi", "C. New York", "D. Moscow")
]

answers = ("A", "A", "D", "B", "C", "B")

guesses = []
score = 0

print("Welcome to the Quiz!")
print("Please enter the corresponding letter (A, B, C, D) for your answer.")
print("")

for i, question in enumerate(questions):
    print("------------------")
    print(f"Question {i+1}: {question}")
    for option in options[i]:
        print(option)
    
    guess = input("Your answer: ").upper()
    guesses.append(guess)
    
    if guess == answers[i]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The correct answer is: {answers[i]}")

print("------------------")
print("      Quiz Results      ")
print("------------------")
print(f"Total score: {score} / {len(questions)}")

print("Correct Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Your Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

percentage_score = (score / len(questions)) * 100
print(f"\nYour score is: {percentage_score:.2f}%")
