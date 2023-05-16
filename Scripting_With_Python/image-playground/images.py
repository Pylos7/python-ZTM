from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
img.thumbnail((400, 400)) # Good for creating profile pictures
img.save("thumbnail.jpg") # Keeps the aspect ratio under the specified parametters

print(img.size)