months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    user = input("Date: ").strip()
    try:
        if user[0].isnumeric():
            result = convert1(user)
            print(result)
        elif user[0].isalpha():
            result = convert2(user)
            print(result)


    except:
        pass
        main()

def convert1(user):
    data = user.split("/")
    if (int(data[1]) < 31) and (int(data[0]) < 12):
        result = f'{data[2]}-{str(data[0]).zfill(2)}-{str(data[1]).zfill(2)}'
        return result
    else:
        raise Exception

def convert2(user):
    data = user.split(" ")
    if data[0].title() in months and int(data[1].endswith(",")) and (int(data[1][:-1])< 31):
            month = months.index(data[0].title()) + 1
            result =f'{data[2]}-{str(month).zfill(2)}-{data[1][:-1].zfill(2)}'
            return result

    else:
        raise Exception


main()