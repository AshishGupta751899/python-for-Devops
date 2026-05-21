# Create Your Own KBC Game
# Design and implement a quiz game inspired by the popular Kaun Banega Crorepati (KBC)
# game show. The aim of this assignment is to test the user's knowledge through a series of
# multiple-choice questions, track their score, and display statistics at the end of the game. The
# game also provides the flexibility to skip any question.
# Instructions:
# 1. Game Structure:
# ○ The game will consist of 5 multiple-choice questions.
# ○ The user will be asked a question with 4 options (A, B, C, D).
# ○ The user can choose to skip any question they do not want to answer.
# 2. Scoring System:
# ○ Points will be awarded for correct answers as follows:
# ■ Question 1 → 1000 points
# ■ Question 2 → 2000 points
# ■ Question 3 → 3000 points
# ■ Question 4 → 5000 points
# ■ Question 5 → 10000 points
# ○ For incorrect answers, no points will be awarded.
# ○ For skipped questions, no points will be awarded, but the game will continue.
# 3. End of Game Statistics:
# ○ At the end of the game, the following statistics will be displayed:
# ■ Total score accumulated from correct answers.
# ■ Number of correct answers provided by the user.
# ■ Number of skipped questions.
# ■ Number of wrong answers
# User Experience:
# ○ At the beginning of the game, ask the user whether they would like to start or
# not the game.
# ○ Provide the option for the user to skip any question at any point..
# 5. Game Ending:
# ○ The game will end when all the questions have been answered or skipped. The
# user should receive their total score
 
print("Welcome to the KBC Game!")
start_game = input("Do you want to start the game? (yes/no): ").strip().lower()
if start_game != "yes":
    print("Thank you for visiting. Have a nice day!")
    exit() 
score = 0
correct_answers = 0
skipped_questions = 0
wrong_answers = 0
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C",
        "points": 1000
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"],
        "answer": "B",
        "points": 2000
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "C",
        "points": 3000
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A. Gold", "B. Oxygen", "C. Silver", "D. Iron"],
        "answer": "B",
        "points": 5000
    },
    {
        "question": "Who is known as the father of modern physics?",
        "options": ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Nikola Tesla"],
        "answer": "B",
        "points": 10000
    }
]
for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    user_input = input("Enter your answer (A, B, C, D) or type 'skip' to skip: ").strip().upper()
    if user_input == "SKIP":
        skipped_questions += 1
        print("Question skipped.")
    elif user_input == q["answer"]:
        score += q["points"]
        correct_answers += 1
        print("Correct! You've earned {} points.".format(q["points"]))
    else:
        wrong_answers += 1
        print("Wrong answer. No points awarded.")

print("\nGame Over!")
print("Total Score: {}".format(score))
print("Correct Answers: {}".format(correct_answers))
print("Skipped Questions: {}".format(skipped_questions))
print("Wrong Answers: {}".format(wrong_answers))

