from random import choice
from word_options import word_options

chosen_word = choice(word_options).lower()
print(f"The word has {len(chosen_word)} characters.")
lives = 5
guessed_letters = []
correct_letters = []

game_over = False

while not game_over:
    print(f"Guessed letters: {guessed_letters}")
    guess_letter = input(f"You have {lives}. Guess a new letter: ").lower()
    if guess_letter in guessed_letters:
        print("You have already guessed that letter.")
    else:
        guessed_letters.append(guess_letter)
        display = ""
        if guess_letter in chosen_word:
            for letter in chosen_word:
                if letter == guess_letter:
                    display += letter
                    correct_letters.append(letter)
                elif letter in correct_letters:
                    display += letter
                else:
                    display += "_"

            if "_" not in display:
                print(f"Congrats! You won with {lives} lives and the word was {display}.")
                game_over = True
        else:
            print("Sorry, that's not the right letter.")

        print(display)
        if guess_letter not in chosen_word:
            lives -= 1
            if lives == 0:
                print("Sorry, you lost!")
                game_over = True