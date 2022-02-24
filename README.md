# Auto-OCR-Screenshot-Directory

I have a huge directory of almost 20,000 screenshots I've taken over the years, and sometimes want to find a screenshots without knowing specifically when I took it.  This script uses Google Tesseract to run OCR on all the screenshots in the directory structure, and generates a .txt file for each one, which can then be searched in windows explorer.

## The Screenshot Directory 
![image](https://user-images.githubusercontent.com/11169730/155574804-d971b442-f26f-45bf-8b15-4f57ae8a3945.png)

## The OCR Text Directory
![image](https://user-images.githubusercontent.com/11169730/155574968-d7bba383-af86-4669-875f-177a35df3726.png)

The script will automatically skip files it has OCR'd before, which makes it easy to set to run on a schedule to periodically update your screenshots folder.  I have a scheduled task set up to run this script every night.

* ocr_directory.py is the main file.
* setup.py is a py2exe config file I wrote for generating an .exe to use with scheduled tasks/crontab.
* [Google Tesseract](https://github.com/tesseract-ocr/tesseract) is required for this script to run.  If you don't install it to the default location, change the path defined for the tesseract.exe file. I used the [windows installer provided by UB Mannheim.](https://github.com/UB-Mannheim/tesseract/wiki)
