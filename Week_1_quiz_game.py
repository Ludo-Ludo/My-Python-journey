# quiz game: user answers questions, and and the end the user will get the result.

print("Welcome to the quiz game!")
playing = input("Are you ready to begin? ").lower()
if playing != "yes":
    quit()

print("Let's begin!")

user_score = 0

answer = input("What is the capital of Italy? ").lower()
if answer == "rome":
    print("Well done!")
    user_score += 1
else:
    print("That's wrong")

answer = input("What is the capital of France? ").lower()
if answer == "paris":
    print("Well done!")
    user_score += 1
else:
    print("That's wrong")

answer = input("What is the capital of Spain? ").lower()
if answer == "madrid":
    print("Well done!")
    user_score += 1
else:
    print("That's wrong")

print(f"Quiz over: you scored {user_score} points!")
