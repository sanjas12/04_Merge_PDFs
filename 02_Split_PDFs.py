from PyPDF2 import PdfFileReader, PdfFileWriter
import sys


def pdf_splitter(path, pages):

    pdf = PdfFileReader(path)

    for page in pages:
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(int(page)-1))

        output_filename = f'page_{page}.pdf'

        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

        print(f'Created: {output_filename}')


# через консоль
if __name__ == '__main__':
    pdf_splitter(sys.argv[1], sys.argv[2:])

