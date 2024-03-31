import random
import time


def print_move(player, row_index, sticks_taken):
    print(f"{player} took {sticks_taken} stick(s) from row {row_index + 1}.")


user_wins = 0
cpu_wins = 0
play_again = True

# Prompt the user for their name
user_name = input("Enter your name: ")
while play_again:
    # Randomly select whether the user or CPU will go first
    current_player = random.choice(["User", "CPU"])

    # Print the game starting message
    print(f"Game starting! {current_player} goes first.")
    print("Generating sticks, get ready!")

    # Create the sticks list
    sticks = [1, 3, 5, 7]

    # Loop while there are sticks remaining
    while sum(sticks) > 0:
        # Print the remaining sticks in rows in a pyramid shape
        for i, row in enumerate(sticks, start=1):
            print(f"{i}:\t" + "\t " * (len(sticks) - i) + "\t ".join(["|" for _ in range(row)]))

        if current_player == "User":
            # Prompt the user for input
            valid_input = False
            while not valid_input:
                try:
                    row_index_input = input(f"{user_name}, enter the row number (1-4): ")
                    if row_index_input.lower() == 'q':
                        print("Thanks for playing!")
                        exit()
                    row_index = int(row_index_input) - 1
                except ValueError:
                    print("Invalid row number. Try again.")
                    continue
                except KeyboardInterrupt:
                    print("\nExiting the game...")
                    exit()

                if row_index < 0 or row_index >= len(sticks):
                    print("Invalid row number. Try again.")
                    continue
                sticks_to_take = int(input(f"How many sticks do you want to take from row {row_index + 1}? "))
                if sticks_to_take < 1 or sticks_to_take > sticks[row_index]:
                    print(f"Invalid number of sticks. You can take between 1 and {sticks[row_index]} from this row.")
                    continue
                valid_input = True
            sticks[row_index] -= sticks_to_take
            print_move("You", row_index, sticks_to_take)
            current_player = "CPU"
        else:
            # CPU's turn
            valid_move = False
            while not valid_move:
                row_index = random.randint(0, len(sticks) - 1)
                if sticks[row_index] == 0:
                    continue  # Skip this row if there are no sticks
                sticks_to_take = random.randint(1, sticks[row_index])
                valid_move = True

            # Add a short delay to make it look like the CPU is thinking
            time.sleep(0.5)  # Delay for 0.5 seconds

            sticks[row_index] -= sticks_to_take
            print_move("CPU", row_index, sticks_to_take)
            current_player = "User"

    # Game over
    print("Game Over!")
    if current_player == "User":
        cpu_wins += 1
        print("CPU wins!")
    else:
        user_wins += 1
        print(f"{user_name} wins!")

    # Ask the user if they want to play again
    play_again = input("Would you like to play again? (y/n) ").lower()
    if play_again == "y":
        play_again = True
    else:
        print(f"You have {user_wins} time(s) and lost {cpu_wins} time(s)")
        print("Thanks for playing!")
        play_again = False
