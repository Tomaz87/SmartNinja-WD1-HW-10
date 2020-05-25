import datetime
import random
import json

player_name = input(f"Hello, what's your name? ")
secret = random.randint(1, 30)
attempts = 0
wrong_guesses = []

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    ordered_score_list = sorted(score_list, key=lambda t: t['attempts'])[:3]

    for score_dict in ordered_score_list:
        print(f'attempts: {score_dict["attempts"]}, date: {score_dict.get("date")}, name: {score_dict.get("name")}, secret number: {score_dict.get("secret_number")}, wrong guesses: {score_dict.get("wrong_guesses")}')

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print(f"You've guessed it - congratulations! It's number {secret}")
        print(f"Attempts needed: {attempts}")
        score_list.append(
            {
                "attempts": attempts,
                "date": str(datetime.datetime.now()),
                "name": player_name,
                "secret_number": secret,
                "wrong_guesses": wrong_guesses
            }
        )

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

    wrong_guesses.append(guess)
