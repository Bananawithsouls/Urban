from PIL import Image, ImageFilter

# Открытие изображения
image = Image.open('123.jpg')

# Изменение размера
image_resized = image.resize((200, 200))
image_resized.save('4.jpg')

# Применение размытия
image_blurred = image.filter(ImageFilter.BLUR)
image_blurred.save('5.jpg')
