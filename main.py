from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import QVariantAnimation
from operation import Task
import datetime, time
import speech_recognition as sr


class AnimationTextEdit(QTextEdit):
    def __init__(self, *args, **kwargs):
        QTextEdit.__init__(self, *args, **kwargs)
        self.animation = QVariantAnimation(self)
        self.animation.valueChanged.connect(self.moveToLine)

    
    def startAnimation(self,max_val):
        self.animation.stop()
        self.animation.setStartValue(max_val)
        self.animation.setEndValue(self.verticalScrollBar().maximum())
        self.animation.setDuration(self.animation.endValue()*4)
        self.animation.start()
    
    def getMax(self):
        return self.verticalScrollBar().maximum()
    
    def moveToLine(self, i):
        self.verticalScrollBar().setValue(i)

class Home_Form(object):
    def setupUi(self, Form):

        self.tick = False
        Form.setObjectName("Windows Assistant")
        Form.resize(473, 128)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input_box = QtWidgets.QLineEdit(Form)
        self.input_box.setWhatsThis('Enter Command here')
        self.input_box.setObjectName("input_box")
        self.horizontalLayout.addWidget(self.input_box)
        self.tick_button = QtWidgets.QPushButton(Form)
        self.tick_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Icons/tick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tick_button.setIcon(icon)
        self.tick_button.setIconSize(QtCore.QSize(25, 25))
        self.tick_button.setObjectName("tick_button")
        self.horizontalLayout.addWidget(self.tick_button)
        self.mic_button = QtWidgets.QPushButton(Form)
        self.mic_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Icons/blue_mic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mic_button.setIcon(icon1)
        self.mic_button.setIconSize(QtCore.QSize(25, 25))
        self.mic_button.setObjectName("mic_button")
        self.horizontalLayout.addWidget(self.mic_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.status_box = AnimationTextEdit(Form)
        self.status_box.setEnabled(True)
        self.status_box.setInputMethodHints(QtCore.Qt.ImhNone)
        self.status_box.setReadOnly(True)
        self.status_box.setObjectName("status_box")
        self.status_box.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.status_box.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.verticalLayout.addWidget(self.status_box)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Windows Assistant"))
        self.label.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Windows Assistant</span></p></body></html>"))
        self.status_box.setFontWeight(100)
        self.status_box.setFontFamily('Arial')
        self.status_box.setFontPointSize(8)

        self.status_updater('󠁗Welcome')
        self.status_updater('How may I help you ❓')
        
        
        

        # Button event
        self.tick_button.clicked.connect(self.read_input)
        self.mic_button.clicked.connect(self.listen_update)

        #Shortcut
        Shortcut = QtWidgets.QShortcut(QtGui.QKeySequence('Return'),Form)
        Shortcut.activated.connect(self.read_input)
        Shortcut = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+m'),self.input_box)
        Shortcut.activated.connect(self.listen_update)

    def status_updater(self,line):
        localtime = time.asctime( time.localtime(time.time()) )
        self.status_box.insertPlainText(str(localtime) + f' : {line} \n')
        self.status_box.startAnimation(self.status_box.getMax())

    def read_input(self):
        self.tick = True
        text = self.input_box.text()
        if text == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Input is Empty')
            msg.setWindowTitle('Warning')
            msg.exec_()
        else:
            self.doTask(text)

    def doTask(self, text):
        event = Task()
        self.status_updater(event.do(text))

    def listen_update(self):
        self.status_updater('listening....')    
        self.mic_on()

    def mic_on(self):
        text = self.listen()
        self.input_box.setText(text)
        self.doTask(text)

    def listen(self):
        sample_rate = 48000

        chunk_size = 2048

        r = sr.Recognizer() 
        
        with sr.Microphone( sample_rate = sample_rate, chunk_size = chunk_size) as source: 
            
            r.adjust_for_ambient_noise(source) 
            
            
            print ("Say Something")
            audio = r.listen(source) 
                
            try: 
                text = r.recognize_google(audio) 
                return (text)
                
            except sr.UnknownValueError: 
                return ("Google Speech Recognition could not understand audio") 
                
            
            except sr.RequestError as e: 
                return("Could not request results from Google Speech Recognition service; {0}".format(e)) 
                
            # finally:
                # self.backgroud(None,None)

    # def backgroud(self,rec_instance,text):
    #     sample_rate = 48000

    #     chunk_size = 2048

    #     r = sr.Recognizer() 
    #     mic = sr.Microphone( sample_rate = sample_rate, chunk_size = chunk_size)
    #     if (('hey' or 'hi' and 'Assistant') in text):
    #         self.listen()
    #     r.listen_in_background(mic,self.backgroud)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Home_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
