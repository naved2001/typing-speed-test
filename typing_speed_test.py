import time
import msvcrt
import winsound
from sentence_api import get_random_sentence


def choose_sentence():
    print("\n===== Sentence Selection =====")
    print("1. Generate Random Sentence")
    print("2. Enter Your Own Sentence")
    while True:
        choice = input("\nChoose option (1/2): ")

        if choice == "1":
            sentence = get_random_sentence()

            if sentence:
                print("\nRandom sentence generated:")
                print(sentence)
                return sentence

            print("API failed. Please enter your own sentence.")

        elif choice == "2":
            while True:
                sentence = input("\nEnter your sentence: ").strip()

                if sentence:
                    return sentence

                print("Sentence cannot be empty.")

        else:
            print("Please choose 1 or 2.")


def get_time_limit():
    while True:
        try:
            limit = int(input("\nEnter time limit (seconds): "))
            if limit <= 0:
                print("Please enter a number greater than 0.")
            else:
                return limit

        except ValueError:
            print("Please enter a valid number.")


def typing_test(sentence, limit):
    print("\nPress Enter to start...")
    input()

    print("\nStart typing:")
    print()

    typed = ""
    start_time = time.time()

    while time.time() - start_time < limit:

        if msvcrt.kbhit():

            key = msvcrt.getwch()

            # Enter key
            if key == "\r":
                break

            # Backspace
            elif key == "\b":
                if typed:
                    typed = typed[:-1]
                    print("\b \b", end="", flush=True)

            # Normal character
            else:
                typed += key
                print(key, end="", flush=True)

    time_taken = time.time() - start_time

    return typed, time_taken


def calculate_wpm(typed, time_taken):
    words = len(typed.split())
    if time_taken <= 0:
        return 0

    wpm = (words / time_taken) * 60

    return round(wpm, 2)

def calculate_accuracy(sentence, typed):
    
    if not typed:
        return 0

    correct_characters = 0

    for expected, actual in zip(sentence, typed):
        if expected == actual:
            correct_characters += 1

    accuracy = (correct_characters / len(sentence)) * 100   

    return round(accuracy, 2)

def calculate_character_stats(sentence, typed):
    correct = 0
    wrong = 0

    for i, character in enumerate(typed):

        if i < len(sentence) and character == sentence[i]:
            correct += 1
        else:
            wrong += 1

    return correct, wrong


def main():
    print("=" * 40)
    print(" TYPING SPEED TEST")
    print("=" * 40)
    sentence = choose_sentence()

    print("\nYour sentence:")
    print(sentence)

    limit = get_time_limit()

    typed, time_taken = typing_test(sentence, limit)

    # Check whether time limit was reached
    if time_taken >= limit:
        print("\n\nTime's up!")
        winsound.Beep(1000, 700)
    else:
        print("\n\nTest finished!")

    wpm = calculate_wpm(typed, time_taken)
    accuracy = calculate_accuracy(sentence, typed)
    correct, wrong = calculate_character_stats(sentence, typed)

    print("\n" + "=" * 40)
    print("              RESULT")
    print("=" * 40)

    print(f"Words typed  : {len(typed.split())}")
    print(f"Time taken   : {round(time_taken, 2)} seconds")
    print(f"Typing speed : {wpm} WPM")
    print(f"Accuracy     : {accuracy}%")
    print(f"Correct chars: {correct}")
    print(f"Wrong chars  : {wrong}")

    print("=" * 40)


if __name__ == "__main__":
    main()