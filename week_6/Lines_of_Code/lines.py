import sys

def main():
    try:
        commands = len(sys.argv)
        if commands < 2:
            sys.exit("Too few command-line arguments")
        elif commands > 2:
            sys.exit("Too many command-line arguments")
        else:
            if sys.argv[1].endswith(".py"):
                with open(sys.argv[1], 'r') as file:
                    print(count_lines(file))
            else:
                sys.exit("Not a python file")
    except FileNotFoundError:
        sys.exit("File does not exist")

def count_lines(f):
    filename = f.readlines()
    number = 0
    for lines in filename:
        if lines.isspace() or lines.lstrip().startswith("#") or lines.strip() == '""':
            pass
        else:
            number += 1
    return number

if __name__ == "__main__":
    main()