import PyPDF2
import os
os.chdir('/home/rahaz/Downloads/')
pdf_file =open('Automate the Boring Stuff with Python (1).pdf','rb')
reader = PyPDF2.PdfFileReader(pdf_file)
reader.numPages
page =reader.getPage(0)
print(page.extractText())