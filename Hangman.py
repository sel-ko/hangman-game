#day 7
import random
import hangman_words
import hangman_art

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)

lives = 6
print(f"Psst.The word is {chosen_word}")
#to make blanked form of letters
display = []
for i in chosen_word:
    display += "_"


game_end = False

while not game_end:
    guess = input("Guess a letter: ").lower()

    #to show if letter is present or not
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter        
    print(f'{" ".join(display)}')

    if guess in display:
      print(f"You already guessed {guess}")
    
  # to check if guess is wrong
    if not guess in chosen_word :
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      print(hangman_art.stages[lives])
      lives -= 1
      if lives == 0:
        print(hangman_art.stages[lives])
        game_end = True
        print("You lose!")

    if "_" not in display:
        game_end = True 
        print("You win!")