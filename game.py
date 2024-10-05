import time
import random

PURPLE = '\033[0;35m'
CYAN = "\033[36m"


def display_menu():
    print("Hello welcome to my script")
    time.sleep(1)
    print("Would you like to play a game? (please only answer in lowercase)")
    return input().strip().lower()


def display_banner():
    banner = (f"""{PURPLE}██████   █████  ███    ███ ███████   
██       ██   ██ ████  ████ ██        
██   ███ ███████ ██ ████ ██ █████     
██    ██ ██   ██ ██  ██  ██ ██        
 ██████  ██   ██ ██      ██ ███████   
                                     


███    ███ ███████ ███    ██ ██    ██ 
████  ████ ██      ████   ██ ██    ██ 
██ ████ ██ █████   ██ ██  ██ ██    ██ 
██  ██  ██ ██      ██  ██ ██ ██    ██ 
██      ██ ███████ ██   ████  ██████  
                                     """)
    print(banner)


def choose_word():
    words = ["python", "hangman", "programming", "development", "posture", "meet", "challenge"]
    return random.choice(words)


def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |   |
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |
           |
           -
        """,
        """
           -----
           |   |
           |
           |
           |
           -
        """,
        """
           -----
           |
           |
           |
           |
           -
        """
    ]
    return stages[tries]


def play_hangman():
    word = choose_word()
    word_length = len(word)
    guessed = ["_"] * word_length
    tries = 6
    guessed_letters = set()

    print("Welcome to Hangman!")

    while tries > 0 and "_" in guessed:
        print(display_hangman(tries))
        print("Current word: " + " ".join(guessed))
        print("Guessed letters: " + " ".join(sorted(guessed_letters)))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed[index] = guess
            print("Good guess!")
        else:
            tries -= 1
            print(f"Wrong guess! You have {tries} tries left.")

    if "_" not in guessed:
        print(f"Congratulations! You've guessed the word: {word}")
    else:
        print(display_hangman(tries))
        print(f"Sorry, you lost! The word was: {word}")


def main():
    while True:
        play_game = display_menu()

        if play_game == 'no':
            print("Quitting script.")
            time.sleep(2)
            break
        elif play_game == 'yes':
            print("Loading games...")
            time.sleep(2)
            display_banner()
            print(f"{CYAN}(1) Hangman\n(2) Quit")
            answer = input("Choose an option: ")

            if answer == '1':
                play_hangman()
            elif answer == '2':
                print("Quitting script.")
                break
            else:
                print("Invalid option. Please choose again.")
        else:
            print("Invalid response. Please answer 'yes' or 'no'.")


if __name__ == "__main__":
    main()












