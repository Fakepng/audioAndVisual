# audioAndVisual

Batch files for audio and visual at SW2

| Name        | Description                                                                   | Version |
| ----------- | ----------------------------------------------------------------------------- | ------- |
| folder      | Use to create and separate `.jpeg`, `raw`, and `.mp4` files into folders      | 1.1.4   |
| pick        | Use to choose which files to use and rename all file base on their date taken | 0.1.1   |
| exifRemover | Use to remove all exif data from files                                        | 0.1.3   |
| owner       | Mass rename file                                                              | 0.0.2   |

---

## folder

> Use to create and separate `.jpeg`, `raw`, and `.mp4` files into folders **_Version: 1.1.4_**

### Before using[^1]

1. Edit the `folder.bat` file in your favorite text editor
2. Change the `RAWEXTENSION` in line 7 variable to the extension of your raw files
3. Save the file

### How to use

1. Run `folder.bat`
2. At the prompt `What Directory would you like?: `, enter the path to the folder containing the files to be separated
3. If raw files are present, the script will create a folder called `RAW` and move all raw files into it
4. The script will then create a folder called `JPEG` and move all `.jpeg` files into it
5. If `.mp4` files are present, the script will create a folder called `VIDEO` and move all `.mp4` files into it

#### Notes

[^1]: If you are using a different camera, you do not need to change the `RAWEXTENSION` variable. The script will prompt you for the extension of your raw files.

---

## pick

> Use to choose which files to use and rename all file base on their date taken **_Version: 0.0.2_**

### How to use

1. Run `pick.exe`
2. At first prompt, enter the path to the folder containing the files to be pick
3. At second prompt, enter the path to the folder where the files will be copied to
4. Type the name of the file you want to copy and press enter[^2]

#### Notes

[^2]: Note that it is not necessary to type every character of the file name. The script will search for the file name and copy the first file that matches the search.

---

## exifRemover

> Use to choose which files to use and rename all file base on their date taken **_Version: 0.1.3_**

### How to use

1. Run `exifRemover.exe`
2. At first prompt, enter the path to the folder containing the files to be exif removed

---

## owner

> Mass rename file **_Version: 0.0.2_**

### How to use

1. Run `owner.exe`
2. At first prompt, enter the path to the folder containing the files to be renamed
3. At second prompt, enter the section of the file name to be renamed[^3]
4. At third prompt, enter the owner name for the section of the file name

#### Notes

[^3]: If left blank, owner name will be added to the front of the file name.

---
