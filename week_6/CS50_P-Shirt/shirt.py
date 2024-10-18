import sys
from PIL import Image,ImageOps


def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        try:
            imagein = sys.argv[1].lower()
            imageout = sys.argv[2].lower()
            if imagein.split(".")[1] == imageout.split(".")[1]:
                if imagein.endswith(".jpg") or imagein.endswith(".jpeg") or imagein.endswith(".png"):
                    photo(imagein, imageout)
                else:
                    sys.exit("Invalid Input")
            else:
                sys.exit("Input and output have different extensions")

        except FileNotFoundError:
            sys.exit("Input does not exist")

def photo(imagein, imageout):
    file = open(imageout, "w")
    with Image.open(imagein) as im1:
        with Image.open("shirt.png") as im2:
            im1 = ImageOps.fit(im1, im2.size)
            im1.paste(im2,im2)
            im1.save(file)
    file.close()

if __name__ == "__main__":
    main()