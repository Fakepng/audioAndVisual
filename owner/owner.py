#Welcome Sot!
#Pick Version 0.0.1
#Author: Fakepng

import os
import tkinter as tk
from tkinter import filedialog
from alive_progress import alive_bar

root = tk.Tk()
root.withdraw()

def main():
  processImageFolder = filedialog.askdirectory()

  imagesList = os.listdir(processImageFolder)

  filteredImagesList = []

  for image in imagesList:
    if image.endswith(".ini"):
      continue
    filteredImagesList.append(processImageFolder + "/" + image)

  originalName = input("Change this: ")
  ownerName = input("Owner name: ")

  print("Processing...")
  with alive_bar(len(filteredImagesList)) as bar:
    for image in filteredImagesList:
      if originalName == "":
        os.rename(image, image.replace(processImageFolder + "/", processImageFolder + "/" + ownerName))
      else:
        os.rename(image, image.replace(originalName, ownerName))

      bar()

  print("Done!")

if __name__ == "__main__":
  main()