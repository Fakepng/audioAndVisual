#Welcome Sot!
#exifRemover Version 0.0.1
#Author: Fakepng

import os
import threading
from PIL import Image
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

def main():
  threads = []
  folderToProcess = filedialog.askdirectory()

  imagesList = os.listdir(folderToProcess)

  print("Processing...")
  for image in imagesList:
    print("Processing: " + image)
    t = threading.Thread(target=exifRemover, args=(folderToProcess + "/" + image,))
    threads.append(t)
    t.start()


  with alive_bar(len(threads)) as bar:
    for t in threads:
      t.join()
      bar()
  
  print("Done!")

if __name__ == "__main__":
  main()