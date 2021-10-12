from PyPDF2 import PdfFileReader, PdfFileWriter
import glob


def merger(output_path, input_paths):
    pdf_writer = PdfFileWriter()

    for path in input_paths:
        pdf_reader = PdfFileReader(path)

        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)


if __name__ == '__main__':
    paths = glob.glob('0*.pdf')

    # print(paths)

    paths.sort()

    merger('pdf_merger.pdf', paths)
