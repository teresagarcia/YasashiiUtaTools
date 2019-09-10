from tkinter import *
import sys
sys.path.append('src') 
from editor.editor_setup import set_layout
from editor.content_setup import set_title, set_tags, set_credits
import utils.file_utils as utils

translation_txt = sys.argv[1]
original_txt = sys.argv[2]
info_file = sys.argv[3]

if __name__ == '__main__':
    editor = set_layout()

    translation = utils.load_txt(translation_txt)
    original_rom = utils.load_txt(original_txt)
    info = utils.load_dict(info_file)

    editor.nametowidget('title').insert(END, set_title(info['artist'], info['song_name']))
    editor.nametowidget('translation_board').insert(END, translation)
    editor.nametowidget('editing_board').insert(END, original_rom)
    editor.nametowidget('tags').insert(END, set_tags(info['artist'], info['song_name'], info['language']))
    editor.nametowidget('credits').insert(END, set_credits())
    
    editor.mainloop()  

