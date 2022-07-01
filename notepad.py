import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QFileDialog,QAction,QMainWindow, qApp

class NotePad(QWidget):
    def __init__(self):

        super().__init__()

        self.initUI()


    def initUI(self):
        self.text_box = QTextEdit()

        self.clear = QPushButton("Clear")
        self.open = QPushButton("Open")
        self.save = QPushButton("Save")
        
        h_box = QHBoxLayout()

        h_box.addWidget(self.clear)
        h_box.addWidget(self.open)
        h_box.addWidget(self.save)
        
        v_box = QVBoxLayout()

        v_box.addWidget(self.text_box)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.setWindowTitle("NotePad")
        self.clear.clicked.connect(self.clear_text)
        self.open.clicked.connect(self.open_text)
        self.save.clicked.connect(self.save_text)
        
        
    def clear_text(self):
        self.text_box.clear()

    def open_text(self):
        file_name = QFileDialog.getOpenFileName(self,"Open File",os.getenv("Desktop"))

        with open(file_name[0],"r") as file:
            self.text_box.setText(file.read())

    def save_text(self):
        file_name = QFileDialog.getSaveFileName(self,"Save File",os.getenv("Desktop"))

        with open(file_name[0],"w") as file:
            file.write(self.text_box.toPlainText())

class Menu(QMainWindow):
    def __init__(self):
        
        super().__init__()

        self.window = NotePad()

        self.setCentralWidget(self.window)

        self.create_menus()

    def create_menus(self):
        
        menubar = self.menuBar()

        file = menubar.addMenu("File")

        open_file = QAction("Open File",self)
        open_file.setShortcut("Ctrl+O")

        save_file = QAction("Save File",self)
        save_file.setShortcut("Ctrl+S")

        clear_file = QAction("Clear File",self)
        clear_file.setShortcut("Ctrl+F")

        exit = QAction("Exit",self)
        exit.setShortcut("ESC")

        file.addAction(open_file)
        file.addAction(save_file)
        file.addAction(clear_file)
        file.addAction(exit)

        file.triggered.connect(self.response)

        self.setWindowTitle("NotePad")

        self.show()

    def response(self,action):

        if action.text() == "Open File":
            self.window.open_file()

        elif action.text() == "Save File":
            self.window.save_file()
        elif action.text() == "Clear File":
            self.window.clear_file()
        elif action.text() == "Exit":
            qApp.quit()


app = QApplication(sys.argv)
menu = Menu()

sys.exit(app.exec_())




        
        