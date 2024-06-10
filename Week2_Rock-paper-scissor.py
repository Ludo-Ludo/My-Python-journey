import random

user_score = 0
computer_score = 0
options = ["rock", "paper", "scissors"]
user_guess = ""

while True:
    user_guess = input("Type rock/paper/scissors, or Q to quit: ").strip().lower()
    if user_guess == "q":
        break
    if user_guess not in options:
        print("Invalid choice.")
        continue

    computer_guess = random.choice(options)
    print("Computer picked", computer_guess + ".")

    # TIE
    if user_guess == computer_guess:
        print("It's a tie!")
    # WIN: user chooses ROCK, computer chooses SCISSORS
    elif user_guess == options[0] and computer_guess == options[2]:
        print("You win.")
        user_score += 1
    # WIN: user chooses PAPER, computer chooses ROCK
    elif user_guess == options[1] and computer_guess == options[0]:
        print("You win.")
        user_score += 1
    # WIN: user chooses SCISSORS, computer chooses PAPER
    elif user_guess == options[2] and computer_guess == options[1]:
        print("You win.")
        user_score += 1
    else:
        print("You lose.")
        computer_score += 1

print(f"Game over. You won {user_score} times. Computer won {computer_score} times.")