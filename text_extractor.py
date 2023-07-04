import os
import pytesseract
import cv2

def extract_text_from_images(image_folder):
    '''
    Extracts text from a collection of images stored in a folder using Tesseract OCR.
    
    Args:
        image_folder (str): The path to the folder containing the input images.
    
    Returns:
        str: The extracted text concatenated from all the images.
    '''

    # Set the path to the Tesseract OCR executable (change it according to your Tesseract installation)
    pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

    # Initialize an empty string to store the concatenated text
    concatenated_text = ''

    # Loop over the images in the folder
    for filename in sorted(os.listdir(image_folder)):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Load the image
            image_path = os.path.join(image_folder, filename)
            img = cv2.imread(image_path)
            
            # Convert the image to black and white for better OCR
            ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
            
            # Perform OCR on the image
            text = pytesseract.image_to_string(thresh1, config='--psm 6')
            
            # Concatenate the text to the existing text
            concatenated_text += text + '\n'
    
    # Return the concatenated text
    return concatenated_text

