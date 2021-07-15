import random
from words import word_list


def choose_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    guessed = False
    word_completion = "_" * len(word)
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed this letter", guess)
            elif guess not in word :
                print(guess, "is not present in the word.")
                tries -= 1
                guessed_letters.append(guess)
                print(tries,"left")
            else :
                print("good guess")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def main():
    word = choose_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = choose_word()
        play(word)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
