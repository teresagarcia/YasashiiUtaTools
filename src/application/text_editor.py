import sys
sys.path.append('src') 
from data.editor_content import EditorContent
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets
from editor.editor_setup import MainWindow
from editor.content_setup import set_title, set_tags, set_credits, get_language_refs
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

    editor.title.setText(info['title'])
    editor.translation_board.insertPlainText(info['translation'])
    editor.editing_board.insertPlainText(info['original'])
    editor.tags.insertPlainText(info['tags'])
    editor.credits.insertPlainText(info['credits'])
    
    editor.show()
    sys.exit( app.exec_() )

