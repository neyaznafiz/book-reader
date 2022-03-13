
import pyttsx3
import PyPDF2
book = open('pdf/book.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
bro = pyttsx3.init()
for number in range(7, pages):
    page = pdfReader.getPage(number)
    text = page.extractText()
    bro.say(text)
    bro.runAndWait()