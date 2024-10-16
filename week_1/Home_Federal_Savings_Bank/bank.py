def main():
    greeting = input("Greeting: ").lower().strip()
    result = value(greeting)
    print(result)

def value(greeting):
    if greeting[:1] == "h":
        if greeting[:5] == "hello":
            return("$0")
        else:
            return("$20")
    else:
        return("$100")

if __name__ == "__main__":
    main()