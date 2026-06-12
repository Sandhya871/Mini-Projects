questions = ("How many elements are in the periodic table ?: ",
              "Which animal lays the largest eggs ?: ",
              "What is the most abundant gas in earth's atmosphere ?: ",
              "How many bones are there in human body ?: ",
              "Which planet in the solar system is the hottest ?: ")

options = (("A. 116 ","B. 117","C. 118","D. 119"),
           ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
           ("A. Nitrogen","B. Oxygen","C. Carbon dioxide","D. Hydrogen"),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Mercury","B. Venus","C. Earth","D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the Correct answer")
    question_num += 1

print("answers: ",end="")
for answer in answers:
    print(answer,end=" ")
print()

print("guesses: ",end="")
for guess in guesses:
    print(guess,end=" ")
print()

score = int(score/len(questions)*100)
print(f"Your Score is: {score}%")

'''A Python quiz game that tests the user's knowledge through multiple-choice questions and calculates the final score.'''

# OUTPUT
How many elements are in the periodic table ?: 
A. 116 
B. 117
C. 118
D. 119
Enter (A, B, C, D): c
CORRECT!
-----------------
Which animal lays the largest eggs ?: 
A. Whale
B. Crocodile
C. Elephant
D. Ostrich
Enter (A, B, C, D): d
CORRECT!
-----------------
What is the most abundant gas in earth's atmosphere ?: 
A. Nitrogen
B. Oxygen
C. Carbon dioxide
D. Hydrogen
Enter (A, B, C, D): a
CORRECT!
-----------------
How many bones are there in human body ?: 
A. 206
B. 207
C. 208
D. 209
Enter (A, B, C, D): a
CORRECT!
-----------------
Which planet in the solar system is the hottest ?: 
A. Mercury
B. Venus
C. Earth
D. Mars
Enter (A, B, C, D): d
INCORRECT!
B is the Correct answer
answers: C D A A B 
guesses: C D A A D 
Your Score is: 80%
