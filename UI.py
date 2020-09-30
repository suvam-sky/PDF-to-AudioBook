from PyQt5 import QtCore, QtGui, QtWidgets
import pyttsx3
import PyPDF2
import warnings
import threading

warnings.filterwarnings('ignore')


speaker = pyttsx3.init()
start=0
num=0
t1=None


##class Worker(QtCore.QRunnable):
##    '''
##    Worker thread
##    '''
##
##    def __init__(self, file,rate,start):
##        super(Worker, self).__init__()
##        self.file=file
##        self.rate=rate
##        self.start=start
##
##    @QtCore.pyqtSlot()
##    def run(self):
##            
##        book = open(self.file, 'rb')
##        pdfReader = PyPDF2.PdfFileReader(book)
##        pages = pdfReader.numPages
##        
##        speaker.setProperty('rate',self.rate)
##
##        text=''
##
##        for num in range(self.start,pages+1):
##
##        
##            page = pdfReader.getPage(num)
##            text = page.extractText()
##
##
##            speaker.say(text)
##            speaker.runAndWait()

        



class Ui_MainWindow(object):

##    def __init__(self):
##        self.threadpool = QtCore.QThreadPool()
##        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())



    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 150)
        MainWindow.setMinimumSize(QtCore.QSize(500, 150))
        MainWindow.setMaximumSize(QtCore.QSize(500, 150))
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("blue-music-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("blue-music-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("blue-music-icon.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("blue-music-icon.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("blue-music-icon.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("blue-music-icon.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("blue-music-icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("blue-music-icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 371, 20))
        self.lineEdit.setStyleSheet("border-radius:4px;")
        self.lineEdit.setObjectName("lineEdit")
        self.Browse = QtWidgets.QPushButton(self.centralwidget)
        self.Browse.setGeometry(QtCore.QRect(410, 30, 75, 23))
        self.Browse.setStyleSheet("QPushButton#Browse{\n"
"    color: rgb(255, 255, 255);\n"
"    alternate-background-color: rgb(0, 0, 255);\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(72, 132, 238, 255), stop:1 rgba(6, 188, 251, 255));\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#Browse:pressed{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    color: rgb(0, 0, 255);\n"
"}")
        self.Browse.setObjectName("Browse")
        self.Stop = QtWidgets.QPushButton(self.centralwidget)
        self.Stop.setGeometry(QtCore.QRect(20, 100, 75, 23))
        self.Stop.setStyleSheet("QPushButton#Stop{\n"
"    color: rgb(255, 255, 255);\n"
"    alternate-background-color: rgb(0, 0, 255);\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(72, 132, 238, 255), stop:1 rgba(6, 188, 251, 255));\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#Stop:pressed{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    color: rgb(0, 0, 255);\n"
"}")
        self.Stop.setObjectName("Stop")
        self.Play = QtWidgets.QPushButton(self.centralwidget)
        self.Play.setGeometry(QtCore.QRect(410, 100, 75, 23))
        self.Play.setStyleSheet("QPushButton#Play{\n"
"    color: rgb(255, 255, 255);\n"
"    alternate-background-color: rgb(0, 0, 255);\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(72, 132, 238, 255), stop:1 rgba(6, 188, 251, 255));\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#Play:pressed{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    color: rgb(0, 0, 255);\n"
"}")
        self.Play.setObjectName("Play")
        self.Pause = QtWidgets.QPushButton(self.centralwidget)
        self.Pause.setGeometry(QtCore.QRect(320, 100, 75, 23))
        self.Pause.setStyleSheet("QPushButton#Pause{\n"
"    color: rgb(255, 255, 255);\n"
"    alternate-background-color: rgb(0, 0, 255);\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(72, 132, 238, 255), stop:1 rgba(6, 188, 251, 255));\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#Pause:pressed{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    color: rgb(0, 0, 255);\n"
"}")
        self.Pause.setObjectName("Pause")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(130, 100, 42, 22))
        self.spinBox.setMaximum(300)
        self.spinBox.setProperty("value", 120)
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 110, 60, 13))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)


        #BUTTON FUCTIONALITY
        self.Browse.clicked.connect(self.browse)
        self.Play.clicked.connect(self.play)
        self.Pause.clicked.connect(self.pause)


        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Read Aloud"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter File Path"))
        self.Browse.setText(_translate("MainWindow", "Browse"))
        self.Stop.setText(_translate("MainWindow", "Stop"))
        self.Play.setText(_translate("MainWindow", "Play"))
        self.Pause.setText(_translate("MainWindow", "Pause"))
        self.label.setText(_translate("MainWindow", "words / min"))

    def browse(self):        
        fm = QtWidgets.QFileDialog.getOpenFileName(None,"Open File","","Pdf (*.pdf)")
        filename = fm[0]
        self.lineEdit.setText(filename)

    
    def play(self):
        file=self.lineEdit.text()
        rate=self.spinBox.value()
        self.SpeakOut(file,rate,start)
        print(start,t1)
##        worker = Worker()
##        self.threadpool.start(worker)
        
        #t1=threading.Thread(target=self.SpeakOut,args=(file,rate,start,))
        #t1.start()

    def SpeakOut(self,file,rate,start):
        
        print(1)
        book = open(file, 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        print(2)
        speaker.setProperty('rate',rate)

        text=''

        for num in range(start,pages+1):

        
            page = pdfReader.getPage(num)
            text = page.extractText()


            speaker.say(text)
            speaker.runAndWait()
            

        


    def SpeakPause(self):
        speaker.stop()
        start=num
        playing=False
        

    def pause(self):
        self.SpeakPause()
    
        
        
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

