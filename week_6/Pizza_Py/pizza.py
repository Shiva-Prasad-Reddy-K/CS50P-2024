from tabulate import tabulate
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    try:
        filename = sys.argv[1]
        if filename.endswith(".csv"):
            with open(filename,"r") as file:
                lines = file.readlines()
            table = []
            for line in lines[1:]:
                table.append(line.rstrip().split(","))
            headers = lines[0].rstrip().split(",")
            print(tabulate(table,headers,tablefmt = 'grid'))
        else:
            sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit("No such File Exists")