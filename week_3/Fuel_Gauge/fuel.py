def main():
        user_input = input("Fraction: ").strip()
        answer = check(user_input)
        if answer > 100:
            main()
        elif answer >= 99:
            print("F")
        elif answer <= 1:
            print("E")
        else:
            print(f"{answer}%")


def check(user_input):
    while True:
        try:
            numbers = user_input.split("/")
            numerator = numbers[0]
            denominator = numbers[1]
            Perc =  round((int(numerator) / int(denominator)) * 100)
            return Perc
        except (IndexError, ValueError, ZeroDivisionError):
            print()

main()