import sys
sys.path.append('src') 
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets
from editor.editor_setup import MainWindow
from editor.content_setup import set_title, set_tags, set_credits
import utils.file_utils as utils

translation_txt = sys.argv[1]
original_txt = sys.argv[2]
info_file = sys.argv[3]

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    editor = MainWindow()

    translation = utils.load_txt(translation_txt)
    original_rom = utils.load_txt(original_txt)
    info = utils.load_dict(info_file)

    editor.title.setText(set_title(info['artist'], info['song_name']))
    editor.translation_board.insertPlainText(translation)
    editor.editing_board.insertPlainText(original_rom)
    editor.tags.insertPlainText(set_tags(info['artist'], info['song_name'], info['language']))
    editor.credits.insertPlainText(set_credits(info['original_url'], info['transliteration_url'], info['translation_url']))
    
    editor.show()
    sys.exit( app.exec_() )

