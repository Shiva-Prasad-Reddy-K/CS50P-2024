def main():
    t = convert(input("What time is it?").strip())
    if 7.00 <= t <= 8.00:
        print("breakfast time")
    elif 12.00 <= t <= 13.00:
        print("lunch time")
    elif 18.00 <= t <= 19.00:
        print("dinner time")

def convert(time):
    split = time.split(":")
    t = float( int(split[0]) + float(float(split[1]) / 60))
    return t;

if __name__ == "__main__":
    main()