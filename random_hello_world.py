import random
import string
import time


def generate_letter():
    time.sleep(0.01)
    return random.choice(f'{string.ascii_letters} .,')


def print_text_random(text):
    counter = 0
    n_letters = len(text)

    string_until_now = ''
    while counter != n_letters:

        letter = generate_letter()
        # print(letter)

        if letter != text[counter]:
            print(string_until_now + letter)
        else:
            string_until_now += letter
            counter += 1

            print(string_until_now)


if __name__ == '__main__':
    text = 'Levy Marques Nunes'

    print_text_random(text)
