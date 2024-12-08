def main():
    greeting = input("Greeting: ")
    result = value(greeting)
    print(f'${result}')

def value(greeting):
    word = greeting.lower().strip()
    if word[:5] == "hello":
        return 0
    elif word[:1] == "h":
            return 20
    else:
        return 100

if __name__ == "__main__":
    main()
