from PIL import Image
import pytesseract


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    # should install tesseract first by sudo apt install tesseract-ocr
    # sudo apt install libtesseract-dev
    # sudo apt-get install tesseract-ocr-eng tesseract-ocr-chi-sim
    text = pytesseract.image_to_string(Image.open(filename), lang='chi_sim')
    # We'll use Pillow's Image class to open the image and pytesseract to
    # detect the string in the image
    # remove the image filename extension and add .txt
    chi_sim_filename = filename.split('.')[0]+'_chi_sim.txt'
    # write text to .txt file
    with open(chi_sim_filename, 'w') as f:
        f.write(text)

    text = pytesseract.image_to_string(Image.open(filename))
    eng_filename = filename.split('.')[0]+'_eng.txt'
    with open(eng_filename, 'w') as f:
        f.write(text)
