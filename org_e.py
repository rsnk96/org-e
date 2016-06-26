import time
import os
import hashlib
import sys
from shutil import move

import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import ttk

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
		currStatus = "\tDone...\n"
	text = "\rPercent: [{0}] {1:.2f}%".format( "="*int(round(barLength*progress)) + " "*(barLength-int(round(barLength*progress))), progress*100)
	sys.stdout.write(text)
	sys.stdout.flush()

#The first element of each of these lists is the name of the folder
folderNames             = [ 'Other Folders', 'Audio', 'Compressed Files', 'Codes', 'Database Files', os.path.join('Office Files', 'Documents'), 'Emails', 'Executables', 'Fonts', 'Models', 'Videos', 'Images', 'PDFs and Page Layout Docs', os.path.join('Office Files', 'Presentations'), os.path.join('Office Files', 'Spreadsheets'), 'Text and Data Files', 'Torrents', 'Webpages']
audioExtensions         = [ folderNames[1], '.wav', '.mid', '.midi', '.wma', '.mp3', '.ogg', '.rma', '.m4a', 'm3u', '.aif', '.mid' ]
compressedExtensions    = [ folderNames[2], '.zip', '.rar', '.7z', '.gz', '.iso', '.tar', '.zipx', '.pkg', '.gz', '.deb', '.xz', '.bz2', '.tgz']
codeExtensions          = [ folderNames[3], '.py', '.cpp', '.cs', '.xml', '.java', '.c', '.xaml', '.m', '.pyd', '.pyc', '.class', '.h', '.pl', '.sh', '.sln', '.vb', '.vcxproj', '.xcodeproj' ]
databaseExtensions      = [ folderNames[4], '.accdb', '.db', '.dbf', '.mdb', '.pdb', '.sql']
documentExtensions      = [ folderNames[5], '.doc' ,'.docx', '.odf', '.docm', '.dot', '.dotx', '.pages', '.wpd', '.wps' ]
emailExtensions         = [ folderNames[6], '.msg']
exeExtensions           = [ folderNames[7], '.exe' , '.msi', '.apk', '.app', '.bat', '.cgi', '.com', '.gadget', '.jar', '.wsf', '']  #there's a safeguard for folders annyways
fontExtensions          = [ folderNames[8],  '.fnt', '.fon', '.otf', '.ttf']
modellingExtensions     = [ folderNames[9], '.3dm', '.3ds', '.max', '.obj', '.dwg', '.dxf' ]
videoExtensions         = [ folderNames[10], '.avi', '.mp4', '.divx', '.wmv', '.mkv', '.srt', '.3gp', '.flv', '.m4v', '.mov', '.mpg' ]
picExtensions           = [ folderNames[11], '.png', '.jpg', '.jpeg', '.bmp', '.gif', '.ico', '.dcm', '.thm', '.tga', '.svg', '.tif', '.psd', '.ai', '.pspimage' ]
pdfExtensions           = [ folderNames[12], '.pdf', '.indd', '.tex', '.epub' ]
presentationExtenstions = [ folderNames[13], '.ppt' ,'.pptx', '.pptm', '.pot', '.potx', '.potm', '.phm', '.phmx', '.pps', '.ppsx', '.ppam', '.ppa', '.odp', '.key']
spreadsheetExtensions   = [ folderNames[14], '.xls' ,'.xlsx', '.xlsm', '.xlsx', '.xlsb', '.xltx', '.xltm', '.xls', '.xlt', '.xlsx', '.xlam', '.xla', '.xlw', '.ods', 'xlr' ]
textFileExtensions      = [ folderNames[15], '.txt', '.rtf', '.log', '.rst', '.in', '.md', '.csv', '.dat', '.sdf', '.bak', '.tmp',  ]
torrentExtensions       = [ folderNames[16], '.torrent', '.tor', '.torr' ]
webpageExtensions       = [ folderNames[17], '.js', '.htm', '.html', '.css', '.asp', '.aspx', '.cer', '.csr', '.jsp', '.php', '.rss', '.xhtml', '.crx', ]

validExtensions = [videoExtensions, audioExtensions, picExtensions, pdfExtensions, documentExtensions, presentationExtenstions, spreadsheetExtensions, codeExtensions, exeExtensions, compressedExtensions, torrentExtensions, webpageExtensions, textFileExtensions, emailExtensions, databaseExtensions, modellingExtensions, fontExtensions]

def pressed():
	original_directory=''+askdirectory(initialdir='.',title='rsnk says: Please select a directory to E-Organize')
	try:
		print('The chosen directory is ' + original_directory)
	except TypeError:
		print('Please choose a valid directory\n\n')
		time.sleep(5)
		sys.exit(0)
	if(original_directory==''):
		print('Please choose a valid directory\n\n')
		time.sleep(5)
		sys.exit(0)

	new_directory = original_directory

	FileList = os.listdir(original_directory)
	unknownExtensions=[]

	# print('\n')

	pb_hd = ttk.Progressbar(root, orient='horizontal', length=400, mode='determinate')
	pb_hd.place(relx=0.34, rely=0.8)
	for i in range(len(FileList)):
		#print(File)
		humriProgressBar( float(i+1)/len(FileList) )
		pb_hd["value"] = float(i+1)*100/len(FileList) 
		File = FileList[i]
		extension = ''.join(os.path.splitext(File)[1])
		name = ''.join(os.path.splitext(File)[0])
		# ext = extension.strip('.')
		if(File=='desktop.ini'):
			continue
		if os.path.isdir(os.path.join(original_directory,File)):
			continue
			# De-Comment at your own risk
			# if(File in folderNames):
			# 	pass
			# else:
			# 	if(os.path.exists(os.path.join(new_directory, folderNames[0]))) != True:
			# 		os.makedirs(os.path.join(new_directory, folderNames[0]))
			# 	move(os.path.join(original_directory, File), os.path.join(new_directory, folderNames[0], File))
			# continue
		elif recognizeExtension(validExtensions, extension.lower()):
			outerIndex, innerIndex = recognizeExtension(validExtensions, extension.lower())
			# if os.path.exists(os.path.join(new_directory, validExtensions[outerIndex][0], File)):
			# 	Data = open(os.path.join(original_directory, File), 'r').read()
			# 	m = hashlib.sha1()
			# 	m.update(Data)
			# 	h = (m.hexdigest())[0:5]
			# 	file(os.path.join(new_directory, validExtensions[outerIndex][0], name+'-'+h+extension), 'w').write(Data)
			# 	print(File, ' ','-->',' ',name+'-'+h+'.'+validExtensions[outerIndex][0])
			# 	os.remove(os.path.join(original_directory, File))

			if os.path.exists(os.path.join(new_directory, validExtensions[outerIndex][0])):
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



root = tk.Tk()
frame = ttk.Frame(root)
style = ttk.Style()
style.theme_use('vista')		#Otherwise use 'clam'
root.geometry('1366x697')
# root.resizable(0,0)
root.configure(bg='#111017')
background_image=tk.PhotoImage(file='Org-E bg.PNG')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.title('Org E. Declutter Your Life.')
# frame = ttk.Frame(root, borderwidth=0, relief="sunken", width=971, height=309)

# label = ttk.Label(root, text='a', font=('Helvetica', 8), foreground='#eeeeee', justify = tk.CENTER)
# label.pack(anchor='n', fill=tk.NONE, expand=tk.YES)
myButton = ttk.Button(root, text = 'Choose your Folder', command=pressed)
myButton.place(relx=0.45, rely=0.7)

# frame.pack()

# label = ttk.Label(frame, text='\n\n\n\n\tOrg E. Declutter your folders with a single click', font=('Helvetica', 36), background='#334353', foreground='#eeeeee', justify = tk.CENTER)
# # label.pack(anchor='n', fill=tk.NONE, expand=tk.YES)

# lblSearchText = tk.StringVar()
# lblSearchText.set('Hello There! Please Choose your folder')
# label2 = ttk.Label(frame, textvariable=lblSearchText, font=('Helvetica', 8), background='#334353', foreground='#eeeeee', justify=tk.CENTER)
# # label.pack(fill=tk.NONE, expand=tk.YES)

# frame.grid(column=0, row=0, columnspan=30, rowspan=2)
# label.grid(column=15, row=2, columnspan=2)


root.mainloop()


# root = tk.Tk()
# style = ttk.Style()
# style.theme_use('vista')		#Otherwise use 'clam'
# root.title('Org E. A one stop solution to decluttering your life')
# w = tk.Label(root, text="Hello Tkinter!", font="Courier 100").pack()
# tk.Button(root, text = 'Choose your Folder', command=pressed).pack()
# # try:
# # 	os.system('cls')
# # except:
# # 	os.system('clear')
# # print('\n\n\n\nOrg E. Declutter your folders with a single click. Please choose your Directory\n\n')
# # time.sleep(3)

# root.mainloop()
