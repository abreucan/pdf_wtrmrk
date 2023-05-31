import PyPDF2

doc_to_stamp = PyPDF2.PdfFileReader(open('merged.pdf', 'rb'))
stamp = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
stamped_file = PyPDF2.PdfFileWriter()


for i in range(doc_to_stamp.getNumPages()):
    num_pages = doc_to_stamp.getPage(i)
    num_pages.mergePage(stamp.getPage(0))
    stamped_file.addPage(num_pages)

    with open('watermarked_output.pdf', 'wb') as file:
        stamped_file.write(file)
