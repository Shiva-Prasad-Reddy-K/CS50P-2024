file = input("File name: ").strip()
split = file.split(".")
type = split[len(split) - 1].lower()

if type == "gif" or type == "png" :
    print("image/" + type)
elif  type == "jpg" or type == "jpeg":
    print("image/jpeg")
elif type == "pdf" or type == "zip":
    print("application/" + type)
elif type == "txt":
    print("text/plain")
else:
    print("application/octet-stream")