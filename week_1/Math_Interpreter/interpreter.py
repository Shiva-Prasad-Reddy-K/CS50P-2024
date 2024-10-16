input = input("Expression: ").strip()
split = input.split()
x = float(split[0])
y = split[1]
z = float(split[2])
if y =="+":
    print("%.1f" % (x + z))
elif y == "-":
    print("%.1f" % (x - z))
elif y == "*":
    print("%.1f" % (x * z))
elif y == "/":
    print("%.1f" % (x / z))