import sys
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit, QLineEdit, QLabel, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtCore import QSize

class SearchWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(275, 130))    
        self.setWindowTitle("Búsqueda") 
        
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        
        self.artist_label = QLabel(self)
        self.artist_label.setText("Artista")
        self.artist_label.move(40, 10)

        self.artist = QLineEdit(self)
        self.artist.move(100, 10)
        self.artist.resize(120, 30)

        self.song_name_label = QLabel(self)
        self.song_name_label.setText("Canción")
        self.song_name_label.move(40, 50)

        self.song_name = QLineEdit(self)
        self.song_name.move(100, 50)
        self.song_name.resize(120, 30)
        
        self.search_button = QPushButton('Buscar', self)
        self.search_button.setToolTip('Busca la letra de la canción introducida')
        self.search_button.move(70, 90)

        self.search_msg = QMessageBox()
        self.search_msg.setWindowTitle("Buscar")
        self.search_msg.setText("Búsqueda en marcha")
        self.search_msg.setIcon(QMessageBox.Information)