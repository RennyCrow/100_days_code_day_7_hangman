import random
from hangman_art import logo, stages
from  hangman_words import word_list

its_over = False
have_letter = False
lives = 6
display = []
chosen_word = random.choice(word_list)

for _ in chosen_word:
    display.append("_")

print(f"{logo}\n")

while not its_over and lives > 0:      
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}.")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
    else:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = chosen_word[position] 

            if "_" not in display:
                its_over = True

    print(f"{stages[lives]}")
    print(f"{display}") 

if lives > 0:
    print("You won.")
else:
    print("You lose")
    print(f"The word was {chosen_word}")             
