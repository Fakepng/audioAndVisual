#Welcome Sot!
#exifRemover Version 0.1.0
#Author: Fakepng

import os
from PIL import Image
from multiprocessing import Pool
import tkinter as tk
from tkinter import filedialog
from alive_progress import alive_bar

root = tk.Tk()
root.withdraw()

def exifRemover(image):
  imageToProcess = Image.open(image)
  imageData = list(imageToProcess.getdata())
  imageWithoutExif = Image.new(imageToProcess.mode, imageToProcess.size)
  imageWithoutExif.putdata(imageData)
  imageWithoutExif.save(image)
  return image

def main():
  folderToProcess = filedialog.askdirectory()

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
  main()