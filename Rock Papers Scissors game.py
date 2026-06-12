import random 

options = ("rock","paper","scissors")
player = None
computer = random.choice(options)
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"palyer: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")
    play_again = input("Play again? (y/n): ").lower()   # OR  if not input("Play again? (y/n): ").lower()== "y": 
    if not play_again == "y":                           
        running = False

print("Thanks for playing!")

'''The program allows the user to play Rock-Paper-Scissors against the computer,
   displays the result of each round, and supports replaying the game.'''

# OUTPUT 
Enter a choice (rock, paper, scissors): rock
palyer: rock
computer: scissors
You win!
Play again? (y/n): y
Enter a choice (rock, paper, scissors): scissors
palyer: scissors
computer: rock
You lose!
Play again? (y/n): 



