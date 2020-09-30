import pyttsx3
import PyPDF2
import warnings

warnings.filterwarnings('ignore')

speaker = pyttsx3.init()
start=0

def SpeakOut(file,rate,start):
    
    book = open(file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    

    
    speaker.setProperty('rate',rate)

    text=''

    for num in range(start,pages+1):

        page = pdfReader.getPage(num)
        text += page.extractText()


    speaker.say(text)
    speaker.runAndWait()

def SpeakPause():
    speaker.stop()
    
def Browse():
        print('Enter')
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        #dlg.setFilter("Pdf files (*.pdf)")
        filenames = QStringList()

        if dlg.exec_():
          filenames = dlg.selectedFiles()



        print('done')  
