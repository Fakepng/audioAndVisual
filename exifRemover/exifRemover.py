#Welcome Sot!
#exifRemover Version 0.1.3
#Author: Fakepng

import os
from PIL import Image
from multiprocessing import Pool, freeze_support
import tkinter as tk
from tkinter import filedialog
from alive_progress import alive_bar

root = tk.Tk()
root.withdraw()

def exifRemover(image):
  imageToProcess = Image.open(image)
  imageExif = imageToProcess.getexif()
  imageData = list(imageToProcess.getdata())
  imageWithoutExif = Image.new(imageToProcess.mode, imageToProcess.size)
  imageWithoutExif.putdata(imageData)

  if len(imageExif):
    if imageExif[274] == 3:
      imageWithoutExif = imageWithoutExif.transpose(method = Image.Transpose.ROTATE_180)
    elif imageExif[274] == 6:
      imageWithoutExif = imageWithoutExif.transpose(method = Image.Transpose.ROTATE_270)
    elif imageExif[274] == 8:
      imageWithoutExif = imageWithoutExif.transpose(method = Image.Transpose.ROTATE_90)

  imageWithoutExif.save(image)
  return image

def main():
  folderToProcess = filedialog.askdirectory(title='Select a folder')

  if folderToProcess == '':
    print('No folder selected')
    return

  imagesList = os.listdir(folderToProcess)

  filteredImagesList = []

  for image in imagesList:
    if image.endswith(".ini"):
      continue
    filteredImagesList.append(folderToProcess + "/" + image)

  print("Processing...")
  with alive_bar(len(filteredImagesList)) as bar:
    with Pool() as pool:
      results = pool.imap_unordered(exifRemover, filteredImagesList)

      for _ in results:
        bar()
  
  print("Done!")

if __name__ == "__main__":
  freeze_support()
  main()