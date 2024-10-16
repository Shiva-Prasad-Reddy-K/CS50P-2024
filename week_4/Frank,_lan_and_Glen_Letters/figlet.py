
import sys
import pyfiglet
import random

if len(sys.argv) == 1:
    font_style = random.choice(pyfiglet.FigletFont.getFonts())

elif sys.argv[1] == "-f" or sys.argv[1] == "--font":
    font_style = sys.argv[2]
    if font_style not in pyfiglet.FigletFont.getFonts():
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")

text = input("Input: ").strip()
result = pyfiglet.figlet_format(text , font = font_style)
print(f"Output: \n{result}")
