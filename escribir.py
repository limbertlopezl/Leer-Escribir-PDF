import PyPDF2

file=open('ejemplo.pdf','rb')
pdfObj = PyPDF2.PdfFileReader(file)
pdfObj.numPages
page1 = pdfObj.getPage(0)
r=pdfObj.isEncrypted
print(r)

page1.cropBox.getWidth
d=page1.extractText()


pdfWriter=  PyPDF2.PdfFileWriter()
pdfWriter.addPage(page1)
out = open('out.pdf','wb')
pdfWriter.write(out)
out.close()