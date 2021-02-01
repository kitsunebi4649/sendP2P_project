import base64


with open("python-logo.png", 'br') as f1:
    b64_img = base64.b64encode(f1.read())
    print(str(b64_img))


with open("python-logo.txt", "w") as f2:
    f2.write(b64_img.decode())


with open("python-logo.txt", 'r') as f3:
    data = f3.read()
    print(data)


img = base64.b64decode(data.encode())
with open("python-logo2.png", 'bw') as f4:
    f4.write(img)

with open('python-logo.txt', 'r') as f:
    message = f.read()
