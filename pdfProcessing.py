import PyPDF2
import os
import sys

pdfDir = './PDF'
toDir = './newPDF'
pdfFileName = os.path.join(pdfDir, 'dummy.pdf')

print(pdfFileName)
with open(pdfFileName, 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    num_pages = len(reader.pages)
    print(f'The PDF has {num_pages} pages.')
    page = reader.getPage(0)
    print(page.extractText())

    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()

    with open(os.path.join(pdfDir, 'rotated_dummy.pdf'), 'wb') as new_file:
        writer.addPage(page)
        writer.write(new_file)
