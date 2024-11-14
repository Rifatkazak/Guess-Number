import random

def display_welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Your goal is to guess the number correctly within the given attempts.")
    print("Difficulty levels:")
    print(" - Easy: 10 attempts")
    print(" - Medium: 7 attempts")
    print(" - Hard: 5 attempts")

def select_difficulty():
    while True:
        difficulty = input("Select difficulty level (easy, medium, hard): ").strip().lower()
        if difficulty == 'easy':
            return 10
        elif difficulty == 'medium':
            return 7
        elif difficulty == 'hard':
            return 5
        else:
            print("Invalid choice. Please choose 'easy', 'medium', or 'hard'.")

def play_game():
    display_welcome_message()
    
    target_number = random.randint(1, 100)
    attempts_left = select_difficulty()
    attempts_used = 0
    
    print(f"\nYou have {attempts_left} attempts to guess the number.\n")
    
    while attempts_left > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts_used += 1
        attempts_left -= 1

        if guess == target_number:
            print(f"Congratulations! You guessed the number {target_number} correctly in {attempts_used} attempts!")
            break
        elif guess < target_number:
            print(f"Too low! You have {attempts_left} attempts left.")
        else:
            print(f"Too high! You have {attempts_left} attempts left.")

    if attempts_left == 0 and guess != target_number:
        print(f"Sorry, you've run out of attempts! The correct number was {target_number}.")

if __name__ == "__main__":
    play_game()