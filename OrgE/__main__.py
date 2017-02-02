import time
import os
import hashlib
import sys
from shutil import move
import site
from PyQt5 import QtCore, QtGui, QtWidgets

shouldSortOtherFolders=False
shouldSortIntoOSDirectory=0
original_directory=''

#The first element of each of these lists is the name of the folder
folderNames             = [ 'Other Folders', 'Audio', 'Compressed Files', 'Codes', 'Database Files', os.path.join('Office Files', 'Documents'), 'Emails', 'Executables', 'Fonts', 'Designs and Models', 'Videos', 'Images', 'PDFs and Page Layout Docs', os.path.join('Office Files', 'Presentations'), os.path.join('Office Files', 'Spreadsheets'), 'Text and Data Files', 'Torrents', 'Webpages', 'Office Files']
audioExtensions         = [ folderNames[1], '.wav', '.mid', '.midi', '.wma', '.mp3', '.ogg', '.rma', '.m4a', 'm3u', '.aif', '.mid' ]
compressedExtensions    = [ folderNames[2], '.zip', '.rar', '.7z', '.gz', '.iso', '.tar', '.zipx', '.pkg', '.gz', '.deb', '.xz', '.bz2', '.tgz']
codeExtensions          = [ folderNames[3], '.py', '.cpp', '.cs', '.xml', '.java', '.c', '.xaml', '.m', '.pyd', '.pyc', '.class', '.h', '.pl', '.sh', '.sln', '.vb', '.vcxproj', '.xcodeproj' ]
databaseExtensions      = [ folderNames[4], '.accdb', '.db', '.dbf', '.mdb', '.pdb', '.sql', '.db-journal']
documentExtensions      = [ folderNames[5], '.doc' ,'.docx', '.odf', '.docm', '.dot', '.dotx', '.pages', '.wpd', '.wps']
emailExtensions         = [ folderNames[6], '.msg']
exeExtensions           = [ folderNames[7], '.exe' , '.msi', '.apk', '.app', '.bat', '.cgi', '.com', '.gadget', '.jar', '.wsf', '.iss', '']  #there's a safeguard for folders annyways
fontExtensions          = [ folderNames[8],  '.fnt', '.fon', '.otf', '.ttf']
modellingExtensions     = [ folderNames[9], '.3dm', '.3ds', '.max', '.obj', '.dwg', '.dxf', '.psd', '.ai', '.pub', '.pmg' ]
videoExtensions         = [ folderNames[10], '.avi', '.mp4', '.divx', '.wmv', '.mkv', '.srt', '.3gp', '.flv', '.m4v', '.mov', '.mpg', '.webm' ]
picExtensions           = [ folderNames[11], '.png', '.jpg', '.jpeg', '.bmp', '.gif', '.ico', '.dcm', '.thm', '.tga', '.svg', '.tif', '.pspimage' ]
pdfExtensions           = [ folderNames[12], '.pdf', '.indd', '.tex', '.epub' ]
presentationExtenstions = [ folderNames[13], '.ppt' ,'.pptx', '.pptm', '.pot', '.potx', '.potm', '.phm', '.phmx', '.pps', '.ppsx', '.ppam', '.ppa', '.odp', '.key']
spreadsheetExtensions   = [ folderNames[14], '.xls' ,'.xlsx', '.xlsm', '.xlsx', '.xlsb', '.xltx', '.xltm', '.xls', '.xlt', '.xlsx', '.xlam', '.xla', '.xlw', '.ods', 'xlr' ]
textFileExtensions      = [ folderNames[15], '.txt', '.rtf', '.log', '.rst', '.in', '.md', '.csv', '.dat', '.sdf', '.bak', '.tmp',  ]
torrentExtensions       = [ folderNames[16], '.torrent', '.tor', '.torr' ]
webpageExtensions       = [ folderNames[17], '.js', '.htm', '.html', '.css', '.asp', '.aspx', '.cer', '.csr', '.jsp', '.php', '.rss', '.xhtml', '.crx', ]
officeExtensions       = [ folderNames[18], '.one','.pub', '.ini']

validExtensions = [videoExtensions, audioExtensions, picExtensions, pdfExtensions, documentExtensions, presentationExtenstions, spreadsheetExtensions, codeExtensions, exeExtensions, compressedExtensions, torrentExtensions, webpageExtensions, textFileExtensions, emailExtensions, databaseExtensions, modellingExtensions, fontExtensions, officeExtensions]






def recognizeExtension(myList, value):
	for outerI, innerI in enumerate(myList):
		try:
			return (outerI, innerI.index(value))
		except ValueError:
			pass
	return 0

def humriProgressBar(progress):
	currStatus = ""
	barLength=20
	if progress >= 1:
		pass
	text = "\rPercent: [{0}] {1:.2f}%".format( "="*int(round(barLength*progress)) + " "*(barLength-int(round(barLength*progress))), progress*100)
	sys.stdout.write(text)
	sys.stdout.flush()




def pressed():
	# original_directory = str(QtGui.QFileDialog.getExistingDirectory(self, 'Select Directory'))
	# try:
	# 	print('The chosen directory is ' + original_directory)
	# except TypeError:
	# 	print('Please choose a valid directory\n\n')
	# 	time.sleep(5)
	# 	sys.exit(0)
	# if(original_directory==''):
	# 	print('Please choose a valid directory\n\n')
	# 	time.sleep(5)
	# 	sys.exit(0)

	new_directory = original_directory

	FileList = os.listdir(original_directory)
	unknownExtensions=[]

	# print('\n')

	# pb_hd = ttk.Progressbar(root, orient='horizontal', length=400, mode='determinate')
	# pb_hd.place(relx=0.34, rely=0.8)
	for i in range(len(FileList)):
		#print(File)
		humriProgressBar( float(i+1)/len(FileList) )
		# pb_hd["value"] = float(i+1)*100/len(FileList)
		File = FileList[i]
		extension = ''.join(os.path.splitext(File)[1])
		name = ''.join(os.path.splitext(File)[0])
		# ext = extension.strip('.')
		if(File=='desktop.ini'):
			continue
		if os.path.isdir(os.path.join(original_directory,File)):
			if(shouldSortOtherFolders==False):
				continue
			else:
				if(File in folderNames):
					pass
				else:
					if(os.path.exists(os.path.join(new_directory, folderNames[0]))) != True:
						os.makedirs(os.path.join(new_directory, folderNames[0]))
					move(os.path.join(original_directory, File), os.path.join(new_directory, folderNames[0], File))
				continue
		elif recognizeExtension(validExtensions, extension.lower()):
			outerIndex, innerIndex = recognizeExtension(validExtensions, extension.lower())
			if os.path.exists(os.path.join(new_directory, validExtensions[outerIndex][0], File)):
				Data = open(os.path.join(original_directory, File), 'r',encoding='utf-8').read()

				m = hashlib.md5(Data.encode('utf-8'))
				# m.update(Data)
				h = (m.hexdigest())[0:5]
				file=open(os.path.join(new_directory, validExtensions[outerIndex][0], name+'-'+h+extension), 'w')
				file.write(Data)
				print(File, ' ','-->',' ',name+'-'+h+'.'+validExtensions[outerIndex][0])
				os.remove(os.path.join(original_directory, File))

			elif os.path.exists(os.path.join(new_directory, validExtensions[outerIndex][0])):
				move(os.path.join(original_directory, File), os.path.join(new_directory, validExtensions[outerIndex][0], File))
			elif os.path.exists(os.path.join(new_directory, validExtensions[outerIndex][0])) != True:
				os.makedirs(os.path.join(new_directory, validExtensions[outerIndex][0]))
				move(os.path.join(original_directory, File), os.path.join(new_directory, validExtensions[outerIndex][0], File))
		else:
			unknownExtensions.append([extension, File])

	if(len(unknownExtensions)>0):
		for curUExt in unknownExtensions:
			print('\n', curUExt[0], ' extension of file ', curUExt[1],' Unknown. Kindly inform the developer at rsnk96@gmail.com')
	# print('\n\n\n%s has successfully been decluttered!\n\n' %original_directory)
	time.sleep(1)



class Window(QtWidgets.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(0,30,1366,697)
		self.setFixedSize(1366,697)

		palette	= QtGui.QPalette()
		palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap(os.path.join(site.getsitepackages()[0],'OrgE','images','org-e bg.jpg'))))
		self.setPalette(palette)

		self.setWindowTitle('Org-E. Declutter your Life!')
		# self.setWindowIcon(QtGui.QIcon('Org.ico'))

		self.home()

	def home(self):
		self.sortOtherFolders =QtWidgets.QCheckBox(self)
		self.sortOtherFolders.move(125,343)

		self.sortIntoOSFolders =QtWidgets.QCheckBox(self)
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
			shouldSortIntoOSDirectory = 1
		else:
			shouldSortIntoOSDirectory = 0

		global original_directory
		original_directory = str(QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory'))
		if(original_directory==''):
			# print('Please choose a valid directory\n\n')
			QtWidgets.QMessageBox.information(self,'Invalid Directory','Please choose a valid directory', QtWidgets.QMessageBox.Ok)
			# time.sleep(5)
			# sys.exit(0)
		else:
			try:
				print('The chosen directory is ' + original_directory)
			except TypeError:
				print('Please choose a valid directory\n\n')
				time.sleep(5)
				sys.exit(0)
			pressed()
			msgBox = QtWidgets.QMessageBox
			msgBox.information(self,'Operation Completed',original_directory+' decluttered.', QtWidgets.QMessageBox.Ok)

		# file = str(QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory'))

class HoverButton(QtWidgets.QPushButton):

    def __init__(self, parent=None):
        super(HoverButton, self).__init__(parent)
        self.setStyleSheet("background-color:#45786d; font:25px Corbel; color:white; border-style:outset")
        self.setMouseTracking(True)

    def enterEvent(self,event):
        # print("Enter")
        self.setStyleSheet("background-color:#56897e; font:25px Corbel; color: white ;border:1px")

    def leaveEvent(self,event):
        self.setStyleSheet("background-color:#45786d; font:25px Corbel; color: white ;border:1px")

def main():
	app =QtWidgets.QApplication(sys.argv)
	app.setWindowIcon(QtGui.QIcon(os.path.join(site.getsitepackages()[0], 'OrgE', 'images','org-e logo.png')))
	GUI = Window()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()