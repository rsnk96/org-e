from PyQt4 import QtCore, QtGui
import sys


# Encoding Utf-8*
try:
    _from_utf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _from_utf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

# Main Window


class Window (QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle(_from_utf8("Org-E. Declutter your computer in a few clicks!!!"))
        self.setStyleSheet("background-image: url(Org-E Bg.png);")

        # ExitOption
        menu_action1 = QtGui.QAction("Exit", self)
        menu_action1.setShortcut("Ctrl+Q")
        menu_action1.setStatusTip('Exit The App')
        menu_action1.triggered.connect(self.close_application)

        self.statusBar()

        # MenuBar
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('Options')
        file_menu.addAction(menu_action1)

        self.home()

    def home(self):

        # NewLibrary btn
        centralwidget = QtGui.QWidget(self)
        self.mainLayout = QtGui.QVBoxLayout(centralwidget)
        new_lib_btn = QtGui.QPushButton("New Library", self)
        new_lib_btn.setMinimumSize(141, 41)

        # AccessLibrary btn
        access_lib_btn = QtGui.QPushButton("Access Library", self)
        access_lib_btn.setMinimumSize(141, 41)

        # FindNewBooks btn
        find_nbooks = QtGui.QPushButton("Find New Books", self)
        find_nbooks.setMinimumSize(141, 41)

        self.mainLayout.addWidget(new_lib_btn)
        self.mainLayout.addWidget(access_lib_btn)
        self.mainLayout.addWidget(find_nbooks)

        self.mainLayout.setAlignment(QtCore.Qt.AlignCenter)

        self.setCentralWidget(centralwidget)

        self.show()

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Exit',
                                        "Close the application?",
                                        QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()