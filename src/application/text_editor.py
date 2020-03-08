import sys
sys.path.append('src') 
from constants import constants
from data.editor_content import EditorContent
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot
from gui.editor import MainWindow
from editor.content_setup import set_title, set_tags, set_credits, get_language_refs
import utils.file_utils as utils
import json
import jsonpickle
from data.editor_content import EditorContent
from blogger.content_adapter import get_final_content
from blogger.send_blogger_draft import send_draft

content_file = constants.CONTENT
result_file = constants.FINAL_CONTENT

app = QtWidgets.QApplication(sys.argv)
editor = MainWindow()

def show_save_message():
    editor.save_msg.exec_() 

def save_changes():
    new_content = EditorContent()
    new_content.title = editor.title.text()
    new_content.translation = editor.translation_board.toPlainText()
    new_content.original = editor.editing_board.toPlainText()
    new_content.video_code = editor.video_code.toPlainText()
    new_content.tags = editor.tags.toPlainText()
    new_content.credits = editor.credits.toPlainText()
    with open(content_file, 'w') as outfile:
        json.dump(jsonpickle.encode(new_content), outfile)

@pyqtSlot()
def save_changes_show():
    save_changes()
    show_save_message()

@pyqtSlot()
def send_to_blogger():
    save_changes()
    get_final_content(content_file, result_file)
    send_draft(result_file)
    editor.send_draft_msg.exec_() 

def main():
    info = utils.load_json(content_file)
    content = jsonpickle.decode(info)

    editor.title.setText(content.title)
    editor.translation_board.insertPlainText(content.translation)
    editor.editing_board.insertPlainText(content.original)
    editor.tags.insertPlainText(content.tags)
    editor.credits.insertPlainText(content.credits)
    editor.video_code.insertPlainText(content.video_code)

    editor.save_button.clicked.connect(save_changes_show)
    editor.send_button.clicked.connect(send_to_blogger)
    
    editor.show()
    sys.exit( app.exec_() )

if __name__ == '__main__':
    main()    