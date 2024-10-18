import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if time := re.search(r"^(\d{1,2})(:00)? (AM|PM) to (\d{1,2})(:00)? (AM|PM)$",s):
        AM =int(time.group(1))
        PM =int(time.group(4))
        if 0 <= AM <= 12 and 0 <= PM <= 12:
            return assign(time)
    else:
        raise ValueError

def assign(time):
    if time.group(3) == "AM":
        AM = time.group(1)
        PM = time.group(4)
        return format(AM,PM,1)
    elif time.group(3) == "PM":
        AM = time.group(4)
        PM = time.group(1)
        return format(AM,PM,2)

def format(AM,PM,n):
    if n == 1:
        if int(AM) == 12 and int(PM) == 12:
            return f"{('0').zfill(2)}:00 to {str(12).zfill(2)}:00"
        else:
            return f"{(AM).zfill(2)}:00 to {str((int(PM)+12)).zfill(2)}:00"
    elif n == 2:
        return f"{str((int(PM)+12)).zfill(2)}:00 to {(AM).zfill(2)}:00"


if __name__ == "__main__":
    main()