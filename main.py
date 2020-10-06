import pyttsx3
import PyPDF2

book = open('python.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker = pyttsx3.init()

# changing some properties
rate = speaker.getProperty('rate')
print(rate)
speaker.setProperty('rate', 125) # speed
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id) #female voice
for num in range(0, pages):
    page = pdfReader.getPage(0)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()


