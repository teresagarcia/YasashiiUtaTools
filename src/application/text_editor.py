from tkinter import *
import sys
sys.path.append('src') 

translation_txt = sys.argv[1]
original_txt = sys.argv[2]
info_file = sys.argv[3]

if __name__ == '__main__':
    editor = Tk()

    titulo = Entry(editor, width=55)
    titulo.grid(row=0, column=0, columnspan=2)

    translation_board = Text(editor, height=50, width=70)
    translation_board.grid(row=1, column=0, rowspan=2)

    editing_board = Text(editor, height=50, width=70)
    editing_board.grid(row=1, column=1, rowspan=2)

    button = Button(editor, text="Enviar")
    button.grid(row = 3, column=0, columnspan=2)

    tags = Text(editor, height=10, width=25)
    tags.grid(row=1, column=2)

    credits_info = Text(editor, height=25, width=25)
    credits_info.grid(row=2, column=2)

    editor.mainloop()  

