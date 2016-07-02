import sys
from PyQt4 import QtGui, QtCore


shouldSortOtherFolders=False
shouldSortIntoOSDirectory=False


class Window(QtGui.QWidget):

	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(0,30,1366,697)
		self.setFixedSize(1366,697)

		palette	= QtGui.QPalette()
		palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap('Org-E Bg.png')))

		self.setPalette(palette)
		self.setWindowTitle('Org-E. Declutter your Life!')
		self.setWindowIcon(QtGui.QIcon('Org.ico'))

		self.home()

	def home(self):
		self.sortOtherFolders =QtGui.QCheckBox(self)
		self.sortOtherFolders.move(125,343)

		self.sortIntoOSFolders =QtGui.QCheckBox(self)
		self.sortIntoOSFolders.move(125,380)

		quitButton = HoverButton(self)
		quitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
		quitButton.setText('Quit')
		quitButton.move(850,550)
		quitButton.resize(200,100)

		mainButton = HoverButton(self)
		mainButton.setText('Choose Folder')
		mainButton.move(300,550)
		mainButton.resize(300,100)
		mainButton.clicked.connect(self.theMainThing)

		self.show()

	def theMainThing(self):
		global shouldSortOtherFolders, shouldSortIntoOSDirectory
		if self.sortOtherFolders.isChecked():
			shouldSortOtherFolders = True
		else:
			shouldSortOtherFolders = False

		if self.sortIntoOSFolders.isChecked():
			shouldSortIntoOSDirectory = True
		else:
			shouldSortIntoOSDirectory = False

		pressed()
		# file = str(QtGui.QFileDialog.getExistingDirectory(self, 'Select Directory'))

class HoverButton(QtGui.QPushButton):

    def __init__(self, parent=None):
        super(HoverButton, self).__init__(parent)
        self.setStyleSheet("background-color:#45786d; font:25px Corbel; color:white; border-style:outset")
        self.setMouseTracking(True)

    def enterEvent(self,event):
        # print("Enter")
        self.setStyleSheet("background-color:#56897e; font:25px Corbel; color: white ;border:1px")

    def leaveEvent(self,event):
        self.setStyleSheet("background-color:#45786d; font:25px Corbel; color: white ;border:1px")

def run():
	app =QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()