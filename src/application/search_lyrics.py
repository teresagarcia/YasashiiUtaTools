import sys
sys.path.append('src') 
from constants import constants
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot
from search.search_window import SearchWindow
from application.lyrics_extraction import extract_lyrics

app = QtWidgets.QApplication(sys.argv)
search_window = SearchWindow()

@pyqtSlot()
def search_data():
    artist = search_window.artist.text()
    song_name = search_window.song_name.text()
    search_window.search_msg.exec_() 
    extract_lyrics(artist, song_name)

def main():
    search_window.search_button.clicked.connect(search_data)
    
    search_window.show()
    sys.exit( app.exec_() )

if __name__ == '__main__':
    main()    