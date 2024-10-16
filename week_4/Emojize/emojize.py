import emoji

def main():
    input_str = input("Input: ").strip()
    print("Output: " + emoji.emojize(input_str , language = 'alias'))

main()