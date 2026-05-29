import random

username = input("Hello! What is your name?: ")

while True:
    guessesTaken = 0
    minNumber = 1
    maxNumber = 20

    number = random.randint(minNumber, maxNumber)

    print(f"Well, {username}. I am thinking in a number between {minNumber} and {maxNumber}.")

    # Game loop
    while guessesTaken < 6:
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        
        guessesTaken += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            break

    if guess == number:
        print(f"Good job {username}! You guessed my number in {guessesTaken} guesses.")

    else:
        print(f"Game over! The number I was thinking of was {number}.")
    
    play_again = input("\nDo you want to play again? (y/n): ").lower().strip()
    if play_again != 'y' and play_again != 'yes':
        print(f"Thank for playing, {username}! Goodbye.")
        break