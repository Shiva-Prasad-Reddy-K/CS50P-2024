import inflect

try:
    name_list = []
    while True:
        name = input("Name ")
        name_list.append(name)

except EOFError:
    p = inflect.engine()
    mylist = p.join(name_list)
    print(f"Adieu, adieu, to {mylist}")