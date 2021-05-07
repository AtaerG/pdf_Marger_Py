from PyPDF2 import PdfFileMerger

pdf_Introduces = ['1.pdf', '2.pdf']

merger = PdfFileMerger()

for file in pdf_Introduces:
    merger.append(file)

merger.write("res.pdf")
merger.close()

