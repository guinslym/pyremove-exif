import Image

image_file = open('python.png')
image = Image.open(image_file)

# next 3 lines strip exif
data = list(image.getdata())
image_without_exif = Image.new(image.mode, image.size)
image_without_exif.putdata(data)

image_without_exif.save('python.png')