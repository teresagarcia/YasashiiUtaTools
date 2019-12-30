import sys
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit, QLineEdit, QLabel, QPushButton, QMessageBox
from PyQt5.QtCore import QSize

BOARD_WIDTH = 500
BOARD_HEIGHT = 620
UPPER_MARGIN = 5
RIGHT_BOX_X = 1050
RIGHT_BOX_WIDTH = 300

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(1360, 700))    
        self.setWindowTitle("Yasashii Uta Tools") 

        self.translation_board = QPlainTextEdit(self)
        self.translation_board.move(10,45)
        self.translation_board.resize(BOARD_WIDTH, BOARD_HEIGHT)

        self.editing_board = QPlainTextEdit(self)
        self.editing_board.move(530,45)
        self.editing_board.resize(BOARD_WIDTH, BOARD_HEIGHT)
        
        self.title_label = QLabel(self)
        self.title_label.setText("Título")
        self.title_label.move(270, UPPER_MARGIN)

        self.title = QLineEdit(self)
        self.title.move(310, UPPER_MARGIN)
        self.title.resize(440,30)

        self.video_label = QLabel(self)
        self.video_label.setText("Código del vídeo")
        self.video_label.move(RIGHT_BOX_X, 45)

        self.video_code = QPlainTextEdit(self)
        self.video_code.move(RIGHT_BOX_X, 75)
        self.video_code.resize(RIGHT_BOX_WIDTH, 160)

        self.tags_label = QLabel(self)
        self.tags_label.setText("Etiquetas")
        self.tags_label.move(RIGHT_BOX_X, 240)
        
        self.tags = QPlainTextEdit(self)
        self.tags.move(RIGHT_BOX_X,270)
        self.tags.resize(RIGHT_BOX_WIDTH, 80)

        self.credits_label = QLabel(self)
        self.credits_label.setText("Créditos")
        self.credits_label.move(RIGHT_BOX_X, 355)

        self.credits = QPlainTextEdit(self)
        self.credits.move(RIGHT_BOX_X,385)
        self.credits.resize(RIGHT_BOX_WIDTH, 280)

        self.save_button = QPushButton('Guardar', self)
        self.save_button.setToolTip('Guarda para seguir luego')
        self.save_button.move(820,UPPER_MARGIN)
        
        self.send_button = QPushButton('Enviar', self)
        self.send_button.setToolTip('Envía la entrada a Blogger')
        self.send_button.move(930,UPPER_MARGIN)

        self.save_msg = QMessageBox()
        self.save_msg.setWindowTitle("Guardar")
        self.save_msg.setText("Cambios guardados~")
        self.save_msg.setIcon(QMessageBox.Information)
