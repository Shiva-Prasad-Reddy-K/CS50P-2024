import sys

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

else:
    if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        with open(sys.argv[1],"r") as file1:
            lines = file1.readlines()

        with open(sys.argv[2],"w") as file2:
            file2.write("first,last,house\n")
            for line in lines[1:]:
                line = line.split(",")
                last, first, house = line[0][1:], line[1][1:-1], line[2].rstrip()
                file2.write(f'{first},{last},{house}\n')