import pyttsx3 # python text to speech version3
import PyPDF2 # python PDF2
# get a pdf file name to open
book = open('cracking the coding interview.pdf', 'rb')
# declare PDF file reader
pdfReader = PyPDF2.PdfFileReader(book)
# count no.of pages
pages = pdfReader.numPages
print(pages)
# initialize the package
speaker = pyttsx3.init()
# declare a start page index
page = pdfReader.getPage(15)
# extract the text in page variable
text = page.extractText()
# command speaker variable to say something
speaker.say(text)
speaker.runAndWait()