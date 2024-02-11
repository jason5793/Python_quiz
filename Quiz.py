questions=("How many elements are there in the periodic table ?",
          "When did India gain indpendce ? ",
          "What is the largest river in India ?",
          "Which of the following is the highest moutain ? ",
          "Who is the creator of Python program ?",
          "What is the captial of India ")

options=(("A.118","B.120","C.130","D.140"),
        ("A.1947","B.1950","C.1945","D.1946"),
        ("A.Indus River","B.Kaveri","C.Yamuna","D.The Ganges River"),
        ("A.K2 (Mount Godwin Austen) ","B.Mount Everest.","C.Kangchenjunga","D.Cho Oyu"),
        ("A.Graydon Hoare","B.Dennis Ritchie","C.James Gosling","D.Guido van Rossum"),
        ("A.Berlin","B.New Delhi","C.New York","D.Moscow")
        )
Answer=("A","A","D","B","C","B")
guesses=[]
score=0
question_number=0
for question in questions:
    print("------------------")
    print(question)
    for option in options[question_number]:
        print(option)
    
    guess= input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == Answer[question_number]:
        score+=1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{Answer[question_number]} is the correct Answer")
    question_number+=1