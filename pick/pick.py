#Welcome Sot!
#Pick Version 0.1.0
#Author: Fakepng

import os
import shutil
import tkinter as tk
from tkinter import filedialog
from exif import Image

root = tk.Tk()
root.withdraw()

def main():
  originalImageFolder = filedialog.askdirectory()
  processedImageFolder = filedialog.askdirectory()

  imagesList = os.listdir(originalImageFolder)

  while True:
    found = False
    imageName = input("Image name: ")
    if imageName == "exit":
      break
    for image in imagesList:
      if imageName in image:
        found = True
        print(image)
        shutil.copyfile(originalImageFolder + "/" + image, processedImageFolder + "/" + image)
        newImageName = ""
        tag = 0
        with open(processedImageFolder + "/" + image, 'rb') as imageFile:
          imageExif = Image(imageFile)
          processedImageFolderList = os.listdir(processedImageFolder)
          date = imageExif.datetime.replace(":", "").replace(" ", "")
          newImageName = date + f'{tag:03d}'
          for processedImage in processedImageFolderList:
            if newImageName in processedImage:
              tag += 1
              newImageName = date + f'{tag:03d}'

        os.rename(processedImageFolder + "/" + image, processedImageFolder + "/" + newImageName + ".jpg")

      else:
        continue

      if found:
        break

    else:
      print("Image not found")

if __name__ == "__main__":
  main()