import random
import sys

def guess(level):
    while True:
        number = random.randint(1, level)
        while True:
            guess = int(input("Guess: ").strip())
            if guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            else:
                print("Just right!")
                sys.exit()
def main():
    while True:
        try:
           while True:
               level = int(input("Level: ").strip())
               if level > 0:
                   guess(level)
                   break

        except ValueError:
           pass

main()