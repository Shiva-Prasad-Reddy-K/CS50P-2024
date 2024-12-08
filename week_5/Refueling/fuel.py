def main():
    user_input = input("Fraction: ").strip()
    answer = convert(user_input)
    print(gauge(answer))


def convert(fraction):
    while True:
        try:
            numbers = fraction.split("/")
            numerator = numbers[0]
            denominator = numbers[1]
            Perc =  round((int(numerator) / int(denominator)) * 100)
            return Perc
        except (IndexError, ValueError, ZeroDivisionError):
            print()


def gauge(percentage):
    if percentage > 100:
        main()
    elif percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
