from PIL import Image
import ctypes
import resize_img.py

#f = open("C:\\Users\\yuri\\Documents\\Yuri's work\\0. Assorted\\_Script\\_image processing\\Python\\2. Placing images on 1000x1000\\_text\\importFileNih.txt", 'r+', encoding='utf-8')
#importFileName = [line for line in f.read().splitlines()]
#f.close()

#white = (255,255,255)
#image = Image.new('RGB', (1000,1000), white)
#image.save("C:\\Users\\yuri\\Documents\\Yuri's work\\0. Assorted\\_Script\\_image processing\\Python\\2. Placing images on 1000x1000\\ngetest.jpg")

img = Image.open("C:\\Users\\yuri\\Documents\\Yuri's work\\0. Assorted\\_Script\\_image processing\\Python\\2. Placing images on 1000x1000\\SS-22 - GEDEAN.jpg", 'r')
img.convert('RGB')

maxSize = (1000, 1000)
img.thumbnail(maxSize, Image.ANTIALIAS)

img_w, img_h = img.size
white = (255, 255, 255, 255)
background = Image.new('RGB', (1000, 1000), white)
bg_w, bg_h = background.size
offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
background.paste(img, offset)
background.save("C:\\Users\\yuri\\Documents\\Yuri's work\\0. Assorted\\_Script\\_image processing\\Python\\2. Placing images on 1000x1000\\ngetest2.jpg")

###############################

#width = 1000
#height = 1000
#imgOri = Image.open("C:\\Users\\yuri\\Documents\\Yuri's work\\0. Assorted\\_Script\\_image processing\\Python\\2. Placing images on 1000x1000\\SS-22.jpg", 'r')
#imgOri.convert('RGB')
#w, h = imgOri.size

