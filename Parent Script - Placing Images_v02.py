from PIL import Image
import ctypes
from resize_img import resize_image

totalExport = 0
errorExport = 0

parentFolder = "C:\\Users\\yuri\\Documents\\Yuri's work\\0. Assorted\\_Script\\_image processing\\Python\\2. Placing images on 1000x1000\\"

#Reading File From List
f = open(parentFolder + "_text\\" + "importFileNih.txt", 'r+', encoding='utf-8-sig')
importFile = [line for line in f.read().splitlines()]
f.close()

f = open(parentFolder + "_text\\" + "saveFileNih.txt", 'r+', encoding='utf-8-sig')
saveFile = [line for line in f.read().splitlines()]
f.close()

if len(importFile) == len(saveFile):
	hitung = range(len(importFile))
	
	for i in hitung:
	
		#Open an Image
		dirLoadOpenFile = parentFolder + '_images\\before\\'
		#img = Image.open(dirLoadOpenFile + importFile[i])
		try:
			img = Image.open(dirLoadOpenFile + importFile[i])
		except (FileNotFoundError): #catch an error if file doesnt exist
			errorExport = errorExport + 1
			break
			
		checkExt = importFile[i]
		checkExt = checkExt[-3:]
		
		if checkExt == "png":
			img.convert('RGBA')
			#img.putalpha(255)
		else:
			img.convert('RGB')
			
		#Resizing image
		hasilResize = resize_image(img, 1000, 1000, False)

		#Creating white background 1000x1000
		white = (255, 255, 255, 255)
		background = Image.new('RGB', (1000, 1000), white)

		#Placing image on the middle (center) of canvas
		img_w, img_h = hasilResize.size
		bg_w, bg_h = background.size
		offsetMiddle = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
		
		if checkExt == "png":
			background.paste(hasilResize, offsetMiddle, mask=hasilResize)
		else:
			background.paste(hasilResize, offsetMiddle)
			
		#Saving an images
		dirLoadSaveFile = parentFolder + "_images\\after\\"
		background.save(dirLoadSaveFile + saveFile[i])
		
		totalExport = totalExport + 1
else:
	textimportFile = "importFile: " + str(len(importFile))
	textsaveFile = "saveFile: " + str(len(saveFile))
 
	textConcatenate = "Jumlah Text : " + "\n" + textimportFile + "\n" + textsaveFile
	ctypes.windll.user32.MessageBoxW(0, "Jumlah List Text Tidak Sama.\nTolong Check Lagi Ya\n\n" + textConcatenate, "Error", 0)

exportSukses = "Done!\nTotal export = " + str(totalExport)

if errorExport >= 1:
	exportGagal = "Total yang GAGAL = " + str(errorExport)
	exportSukses = exportSukses + "\n" + exportGagal

ctypes.windll.user32.MessageBoxW(0, exportSukses, "Exported", 0)
