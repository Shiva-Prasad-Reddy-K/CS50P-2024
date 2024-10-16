def main():
    try:
        item_list = []
        while True:
            item = input().strip().upper()
            item_list.append(item)
    except EOFError:
        item_list = sorted(item_list)
        print_list(item_list)

def print_list(item_list):
    list2 = []
    for _ in item_list:
        c = 0
        for i in list2:
            if i == _:
                c += 1
                break
        if c == 0:
            number = counter(_,item_list)
            print(f"{number} {_}")
            list2.append(_)

def counter(item, item_list):
    count = 0
    for i in item_list:
        if i == item:
            count += 1
    return count

main()