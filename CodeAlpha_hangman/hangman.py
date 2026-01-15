import random

# Predefined list of words
words = ["python", "apple", "chair", "house", "water"]

# Select a random word
secret_word = random.choice(words)

# convert word to a list of underscores
display_word = ["_"] * len(secret_word)

# Guessed letters
guessed_letters = []

# Number of allowed incorrect guesses
incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman!")
print("You have 6 incorrect guesses.\n")

# Using while loop
while((incorrect_guesses<=max_incorrect) and ("_" in display_word)):
    print("Word:", " ".join(display_word))
    print("Guessed letters:", ", ".join(guessed_letters))
    print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")

    guess = input("Guess a letter:").lower()

    # All conditions handled using if-elif-else
    if((len(guess) != 1) or not (guess.isalpha())):
        print("Please enter a single letter.\n")

    elif(guess in guessed_letters):
        print("You already guessed that letter.\n")

    elif(guess in secret_word):
        print("Correct!\n")
        guessed_letters.append(guess)
        for i in range(len(secret_word)):
            if(secret_word[i] == guess):
                display_word[i] = guess


    else:
        print("Wrong guess!\n")
        guessed_letters.append(guess)
        incorrect_guesses += 1

if("_" not in display_word):
    print("Congratulations! You guessed the word:", secret_word)
else:
    print("Game Over! The word was:", secret_word)

