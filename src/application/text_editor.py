from tkinter import *
import sys
sys.path.append('src') 
import editor.editor_setup as setup

translation_txt = sys.argv[1]
original_txt = sys.argv[2]
info_file = sys.argv[3]

if __name__ == '__main__':
    editor = setup.set_layout()

    editor.nametowidget('title').insert(END, "Arashi - Truth")
    editor.mainloop()  

