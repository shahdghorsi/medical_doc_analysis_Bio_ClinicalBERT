# Medical Record Text Extraction

## Overview
This project aims to extract text from medical records using OCR (Optical Character Recognition) and get crucial information from each given document using Bio_ClinicalBERT to provide the required output.
## Structure
- health_pipeline.py: this file has the mainstream where the extracted text is used to perform the Q&A task running the model.
- pdf_to_img.py: this file is run once only currently to convert the given pdf to image because Tesseract takes images only.
- text_extractor.py: this file uses Tesseract to extract the text from all the images extracted from the pdf. The resulting text is concatenated and returned when the extract_text_from_images function is called.
- output.json: is the file that has the final result in a JSON format.
- output_py2pdf.txt and text_output.py have the output text from Py2PDF and tesseract.
## Requirements
- Python 3.8 or above
- Tesseract OCR
- OpenCV
- PyTesseract
- PDF2Image (optional, if you want to process PDF files instead of using Tesseract)
- PyTorch
- Transformers

## Installation
1. Install Tesseract OCR:
   - On macOS, you can use Homebrew: `brew install tesseract`
   - On Windows, you can download the installer from the official Tesseract OCR website: https://github.com/UB-Mannheim/tesseract/wiki

2. Install Python dependencies:

3. Download the necessary language data for Tesseract OCR:
- Visit the Tesseract OCR GitHub repository: https://github.com/tesseract-ocr/tessdata
- Download the language data files relevant to your use case (e.g., English language data).

4. Set the Tesseract OCR executable path in the code:
- Locate the line `pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract'` in the code.
- Replace `/path/to/tesseract` with the actual path to the Tesseract OCR executable on your system.

## Usage
The main text extraction task in this project is done by the `extract_text_from_image` function provided in the `text_extractor.py` module. This function takes the path to an image file as input and returns the extracted text as a string.
Additionally, the `health_pipeline.py` file includes the main task where Bio_ClinicalBERT is used for question-answering.


