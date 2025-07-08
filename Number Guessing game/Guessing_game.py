import random
import sys
import time

# High score tracker per difficulty
high_scores = {
    "Easy": None,
    "Medium": None,
    "Hard": None
}

def start_game(chance, level_name):
    # Generate a random number between 1 and 100
    generate_no = random.randint(1, 100)
    # Record the start time of the game
    start_time = time.time()
    # Initialize attempt counter
    attempt = 0

    # Loop until user runs out of chances
    while attempt < chance:
        try:
            # Prompt user for their guess and convert to integer
            guess_num = int(input("Enter your guess: "))
        except ValueError:
            # Handle non-integer input
            print("Please enter a valid number!")
            continue

        # Increment attempt counter
        attempt += 1

        if guess_num == generate_no:
            # Calculate duration taken to guess correctly
            duration = round((time.time() - start_time), 2)
            print(f"Congratulations! You guessed the correct number in {attempt} attempts and {duration} seconds")
            
            # Update high score if it's a new record or first score
            if high_scores[level_name] is None or attempt < high_scores[level_name]:
                high_scores[level_name] = attempt
                print(f"🏆 New high score for {level_name} difficulty!")
            else:
                print(f"🎯 Current high score for {level_name}: {high_scores[level_name]} attempts.")

            return  # End the function if guessed correctly

        elif guess_num < generate_no:
            # Inform user their guess is too low
            print(f"Incorrect! The number is greater than {guess_num}.")

        else:
            # Inform user their guess is too high
            print(f"Incorrect! The number is less than {guess_num}.")

    else:
        # User has used all chances
        print("🚫 Your chances are over! Better luck next time.")
        

def main():
    print(
    """   
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
    """)
    
    while True:
        print("""
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
            """)
        
        # Map user input to difficulty and number of chances
        levels = {
            1: ("Easy", 10),
            2: ("Medium", 5),
            3: ("Hard", 3)
        }
        
        while True:
            try:
                # Prompt user to select difficulty level
                level = int(input("Enter Your choice: "))
                if level not in levels:
                    print("Please enter 1, 2, or 3 only.")
                    continue
                break  # Valid input, exit loop
            except ValueError:
                print("Please enter a valid number (1, 2, or 3).")
    
        # Get difficulty name and number of chances
        difficulty, chance = levels[level]
        print(f"Great! You have selected the {difficulty} difficulty level.\nLet's start the game!")
        
        # Start the guessing game
        start_game(chance, difficulty)
        
        # Ask user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("okk!!bye!!!")
            sys.exit()

if __name__ == '__main__':
    main()
