import PyPDF2
import os
import sys

inputs = sys.argv[1:]
print(f'Inputs: {inputs}')


def pdf_watermarker(pdf_list):
    pdfDir = './PDF'
    print(f'Watermarkingg PDFs: {pdf_list}')

    # get the watermark that will be used for all pages of the PDFs
    wtrFile = os.path.join(pdfDir, "wtr.pdf")
    wtr_reader = PyPDF2.PdfFileReader(wtrFile)
    watermark_page = wtr_reader.getPage(0)
    print(f'Watermark page: {watermark_page}')

    # Loop through each PDF file in the list and apply the watermark to each page
    for pdf_file in pdf_list:
        pdf = os.path.join(pdfDir, pdf_file)
        print(pdf)

        # create a new PDF writer to write the watermarked pages to
        watermarkedPdfFile = os.path.join(pdfDir, "watermarked_" + pdf_file)
        pdf_watermarker = PyPDF2.PdfFileWriter()

        # open the PDF file to be watermarked and determine the number of pages
        with open(pdf, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            num_pages = len(reader.pages)
            print(f'The PDF has {num_pages} pages.')

            # create a new file to save the watermarked pages to
            with open(watermarkedPdfFile, 'wb') as new_file:
                # get page add your watermark and write page to new file
                for page_num in range(num_pages):
                    # get the page to be watermarked and merge with watermark
                    page = reader.getPage(page_num)
                    page.mergePage(watermark_page)

                    # write the watermarked page to the new file
                    pdf_watermarker.addPage(page)
                    print(f'Adding watermark to page {page_num}')
                    pdf_watermarker.write(new_file)


pdf_watermarker(inputs)
