from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img = img.convert('L')  # Convert to grayscale
resized_img = filtered_img.resize((300, 300))
resized_img.save('./Pokedex/pikachu_resize.png', 'PNG')

resized_img.show()
# img = Image.open('./Pokedex/pikachu_blurred.png')
# print(dir(img))
print(img.format)
print(img.mode)
