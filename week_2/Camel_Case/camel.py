input = input("camelcase: ").strip()
print("snake_case:" , end = "")
for char in input:
    if char <= "Z" and char >= "A":
        print("_" + chr(ord(char) + 32) , end = "", sep = "")
    else:
        print( char , end = "")