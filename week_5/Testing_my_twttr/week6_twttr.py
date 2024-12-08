def main():
    text = input("Input: ")
    shorten(text)
    result = shorten(text)
    print("Output: ", result, end = "")
    print()

def shorten(word):
    o_word = ""
    for i in word:
        if i in ("a","e","i","o","u","A","E","I","O","U"):
            pass
        else:
            o_word = o_word + i
    return o_word

if __name__ == '__main__':
    main()
