def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    max_len = 6
    min_len = 2
    if min_len <= len(s) <= max_len:
        if s[0].isalpha() and s[1].isalpha():
            if check(s):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def check(text):
    look= len(text)
    while(True):
        look -= 1
        if text[look] != "." and text[look] != "," and text[look] != "?" and text[look] != "!" and text[look] != " " :
            if text[look].isalpha():
                for _ in range(look):
                    if text[_].isalpha():
                        continue
                    else:
                        return False
                if (look + 1) < len(text):
                    if text[look + 1] == "0":
                        return False
                return True
            else:
                continue
        else:
            return False


main()