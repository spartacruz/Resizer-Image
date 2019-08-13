from PIL import Image
import ctypes

def resize_image(img, width=None, height=None, crop=False):
    old_width, old_height = img.size
    current_ratio = old_width / old_height
    if width and height:
        if crop:
            target_ratio = width / height
            if target_ratio < current_ratio:
                new_width = int(width * old_height / height)
                x = (old_width - new_width) // 2
                img = img.crop((x, 0, x + new_width, old_height))
            elif target_ratio > current_ratio:
                new_height = int(height * old_width / width)
                y = (old_height - new_height) // 2
                img = img.crop((0, y, old_width, y + new_height))
        else:
            new_width = int(height * current_ratio)
            new_height = int(width / current_ratio)
            if new_width > width:
                height = new_height
            elif new_height > height:
                width = new_width
    elif width:
        height = int(width / current_ratio)
    elif height:
        width = int(height * current_ratio)

    if width and height:
        img = img.resize((width, height), Image.ANTIALIAS)
    return img

#img = Image.open("C:\\Users\\yuri\\Documents\\Yuri's work\\0. Assorted\\_Script\\_image processing\\Python\\2. Placing images on 1000x1000\\SS-22 - GEDEAN.jpg")
#img.convert('RGB')

#resize_image(img, 1000, 1000, False).save("C:\\Users\\yuri\\Documents\\Yuri's work\\0. Assorted\\_Script\\_image processing\\Python\\2. Placing images on 1000x1000\\ngetest - resize nih 2.jpg")
