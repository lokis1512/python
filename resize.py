from PIL import Image
print(dir(Image))
imgPath = "/home/loki/Downloads/eye.jpg"
img = Image.open(imgPath)
size = (200,200)
o = img.resize(size)
o.show()

