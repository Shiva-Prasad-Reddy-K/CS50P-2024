def main():
    text = input("Input: ")
    shorten(text)
    result = shorten(text)
    print("Output: ", result, end = "")
    print()

def shorten(word):
    o_word = ""
    for i in word:
        if i =="a" or i =="e" or i =="i" or i =="o" or i =="u" or i =="A" or i =="E" or i =="I" or i =="O" or i =="U":
            pass
        else:
            o_word = o_word + i
    return o_word

if __name__ == '__main__':
    main()
