print("Welcome to Rock, Paper, Scissors game!")
print("Choose between 'rock', 'paper', or 'scissors'.")

player1_choice = input("Player 1, enter your choice: ").lower()
player2_choice = input("Player 2, enter your choice: ").lower()

if player1_choice not in ['rock', 'paper', 'scissors'] or \
   player2_choice not in ['rock', 'paper', 'scissors']:
    print("Invalid choice! Please choose between 'rock', 'paper', or 'scissors'.")
else:
    if player1_choice == player2_choice:
        print("It's a tie!")
    elif (player1_choice == "rock" and player2_choice == "scissors") or \
         (player1_choice == "paper" and player2_choice == "rock") or \
         (player1_choice == "scissors" and player2_choice == "paper"):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")