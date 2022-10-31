# audioAndVisual

Batch files for audio and visual at SW2

| Name   | Description                                                              | Version |
| ------ | ------------------------------------------------------------------------ | ------- |
| folder | Use to create and separate `.jpeg`, `raw`, and `.mp4` files into folders | 1.0.0   |

---

## folder

> Use to create and separate `.jpeg`, `raw`, and `.mp4` files into folders **_Version: 1.0.0_**

### Before using[^1]

1. Edit the `folder.bat` file in your favorite text editor
2. Change the `RAWEXTENSION` in line 6 variable to the extension of your raw files
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
