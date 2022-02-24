import glob
from PIL import Image
import pytesseract as pt
import os
import time
import logging
logging.basicConfig(handlers=[logging.FileHandler("ocr_directory.log"), logging.StreamHandler()], format='%(asctime)s | %(levelname)s: %(message)s', level=logging.INFO)

# Setting paths:
# tesseract_path is the location where tesseract.exe is installed
# screenshots_path is the root folder of screenshots to be OCR'd
# ocr_path is the directory where the corresponding .txt files will be written for each screenshot file in screenshots_path
tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
screenshots_path = r"""C:\ShareX Screenshots"""
ocr_path = r"""C:\ShareX Screenshots\_OCR Files"""

# Check if tesseract is installed where we think it should be
if not os.path.exists(tesseract_path):
    raise Exception("Tesseract not installed in expected location at " + tesseract_path)
else:
    logging.info('Found Tesseract installed at ' + tesseract_path + ', using it...')

# Point pytesseract at our install
pt.pytesseract.tesseract_cmd = tesseract_path

# Get a file list of all png, jpg, and jpeg files in the screenshots_path, searching recursively through all subfolders
file_list = glob.glob(screenshots_path + '**/**/*.png', recursive=True) + glob.glob(screenshots_path + '**/**/*.jpg', recursive=True) + glob.glob(screenshots_path + '**/**/*.jpeg', recursive=True)
logging.debug(file_list)
new_file_list = [file.replace(screenshots_path, ocr_path) + '.txt' for file in file_list]

files_scanned = len(file_list)
files_OCRd = 0
files_errord = 0
files_skipped = 0

for file, new_file in zip(file_list, new_file_list):
    if os.path.exists(new_file):
        logging.debug("OCR'd Text Already Exists, Skipping OCR for file " + file)
        files_skipped += 1
    else:
        try:
            img = Image.open(file)
        except Exception as e:
            logging.error("Failed to open image at " + file + " with error " + str(e))
            files_errord += 1
            continue

        text = pt.image_to_string(img, lang="eng")
        os.makedirs(os.path.dirname(new_file), exist_ok=True)
        with open(new_file, 'w') as f:
            f.write(text)
            logging.debug("Wrote text for file at " + new_file)
            files_OCRd += 1

logging.info("Complete.")
logging.info(str(files_scanned) + ' image files scanned')
logging.info(str(files_OCRd) + " new images OCR'd")
logging.info(str(files_errord) + " images not able to be opened")
logging.info(str(files_skipped) + " images skipped (already OCR'd)")
time.sleep(5)
