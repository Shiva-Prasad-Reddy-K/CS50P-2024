import random

def main():
    level = get_level()
    score = 0
    counter = 0
    while counter < 10:
        X,Y = generate_integer(level)
        mistakes = 0
        while True:
            try:
                answer = int(input(f"{X} + {Y} = ").strip())
                if answer == (X+Y):
                     score += 1
                     counter += 1
                     break
                else:
                     print("EEE")
                     mistakes += 1
                if mistakes == 3:
                     print(f"{X} + {Y} = {X+Y}")
                     counter += 1
                     break
            except ValueError:
                 mistakes += 1
                 print("EEE")
                 pass
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if 0 < level < 4:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        X = random.randint(0, 9)
        Y = random.randint(0, 9)
    elif level == 2:
        X = random.randint(10, 99)
        Y = random.randint(10, 99)
    else:
        X = random.randint(100, 999)
        Y = random.randint(100, 999)
    return [X, Y]


if __name__ == "__main__":
    main()