import PyPDF2
import os
import sys

inputs = sys.argv[1:]
print(f'Inputs: {inputs}')
pdfDir = './PDF'


def pdf_combiner(pdf_list):
    writer = PyPDF2.PdfFileWriter()
    print(f'Joining PDFs: {pdf_list}')
    merger = PyPDF2.PdfFileMerger()

    for pdf_file in pdf_list:
        pdf = os.path.join(pdfDir, pdf_file)
        print(pdf)
        merger.append(pdf)

    merger.write(os.path.join(pdfDir, 'merged.pdf'))
    merger.close()


pdf_combiner(inputs)
