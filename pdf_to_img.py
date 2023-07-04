from pdf2image import convert_from_path

pdfs = r"medical-record.pdf"
pages = convert_from_path(pdfs, 350)

i = 1
for page in pages:
    image_name = "Page_" + str(i) + ".jpg"  
    page.save(image_name, "JPEG")
    i = i+1        

'''This code snippet converts a PDF file into a series of JPEG images.
It takes a PDF file path as input and produces JPEG images for each page of the PDF.

Input:

pdfs (str): The path to the PDF file.
Output:
Images extracted from the given pdf