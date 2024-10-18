
from validator_collection import validators

def main():
    s = input("What's your email address? ").strip()
    print(validation(s))

def validation(s):
    try:
        email_address = validators.email(s)
        if email_address:
            return "Valid"
    except ValueError:
        return "Invalid"

if __name__ == "__main__":
    main()