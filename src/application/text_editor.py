import sys
sys.path.append('src') 
from data.editor_content import EditorContent
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot
from editor.editor_setup import MainWindow
from editor.content_setup import set_title, set_tags, set_credits, get_language_refs
import utils.file_utils as utils
import json
import jsonpickle
from data.editor_content import EditorContent

info_file = sys.argv[1]

@pyqtSlot()
def save_changes():
    new_content = EditorContent()
    new_content.title = editor.title.text()
    new_content.translation = editor.translation_board.toPlainText()
    new_content.original = editor.editing_board.toPlainText()
    new_content.video_code = editor.video_code.toPlainText()
    new_content.tags = editor.tags.toPlainText()
    new_content.credits = editor.credits.toPlainText()
    with open(info_file, 'w') as outfile:
        json.dump(jsonpickle.encode(new_content), outfile)
    editor.save_msg.exec_() 

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    editor = MainWindow()

    info = utils.load_json(info_file)
    content = jsonpickle.decode(info)

    editor.title.setText(content.title)
    editor.translation_board.insertPlainText(content.translation)
    editor.editing_board.insertPlainText(content.original)
    editor.tags.insertPlainText(content.tags)
    editor.credits.insertPlainText(content.credits)
    editor.video_code.insertPlainText(content.video_code)

    editor.save_button.clicked.connect(save_changes)
    
    editor.show()
    sys.exit( app.exec_() )

