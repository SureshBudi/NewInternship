import random


def generate_secret_number():
    """Generate a random 4-digit number as the secret number."""
    return random.randint(1000, 9999)


def get_guess_from_player():
    """Get a 4-digit number guess from the player."""
    while True:
        try:
            guess = int(input("Enter your 4-digit guess: "))
            if 1000 <= guess <= 9999:
                return guess
            else:
                print("Please enter a 4-digit number.")
        except ValueError:
            print("Invalid input. Please enter a valid 4-digit number.")


def get_matching_digits(secret, guess):
    """Compare the digits of secret and guess to find matches."""
    secret_str = str(secret)
    guess_str = str(guess)
    matches = sum(1 for s, g in zip(secret_str, guess_str) if s == g)
    return matches


def play_game():
    secret_number = generate_secret_number()
    print("Player 1 has set the secret number. Player 2, it's your turn to guess!")

    attempts = 0
    while True:
        attempts += 1
        guess = get_guess_from_player()

        if guess == secret_number:
            print(f"Congratulations! Player 2 has guessed the number {secret_number} correctly in {attempts} attempts.")
            return attempts

        matches = get_matching_digits(secret_number, guess)
        print(f"Player 2, your guess {guess} has {matches} correct digits.")


def main():
    print("Welcome to the Mastermind game!")
    print("Player 1 will set the secret number and Player 2 will try to guess it.")
    print("Player 2, you will have up to 10 attempts to guess the number.")
    print()

    player2_attempts = play_game()

    print("\nNow, Player 2 has set the secret number. Player 1, it's your turn to guess!")
    print("You will have to guess the number within the same number of attempts Player 2 took.")

    attempts = 0
    while attempts < player2_attempts:
        attempts += 1
        guess = generate_secret_number()  # Player 1's guess is a random number

        print(f"Player 1 guesses {guess}.")  # Normally, Player 1 would input their guesses.

        if guess == secret_number:
            print(f"Congratulations! Player 1 has guessed the number {secret_number} correctly in {attempts} attempts.")
            print("Player 1 is crowned Mastermind!")
            return

    print(f"Player 2 won the game as Player 1 could not guess the number {secret_number} in {attempts} attempts.")
    print("Player 2 is crowned Mastermind!")


if __name__ == "__main__":
    main()
