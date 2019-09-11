from tkinter import *
import tkinter.font as tkFont

BOARD_HEIGHT = 55
BOARD_WIDTH = 80
RIGHT_BOX_WIDTH = 32

def set_layout():
    editor = Tk()

    title_label = Label(editor, text="Título")
    title_label.grid(row=0, column=0)
    
    title = Entry(editor, width=55, name="title")
    title.grid(row=0, column=0, columnspan=2)

    translation_board = Text(editor, height=BOARD_HEIGHT, width=BOARD_WIDTH, name="translation_board")
    translation_board.grid(row=2, column=0, rowspan=5)

    editing_board = Text(editor, height=BOARD_HEIGHT, width=BOARD_WIDTH, name="editing_board")
    editing_board.grid(row=2, column=1, rowspan=5)

    button = Button(editor, text="Enviar")
    button.grid(row=7, column=0, columnspan=2)

    tags_label = Label(editor, text="Etiquetas")
    tags = Text(editor, height=10, width=RIGHT_BOX_WIDTH, name="tags")
    tags_label.grid(row=2, column=2, sticky=S)
    tags.grid(row=3, column=2, sticky=N)

    credits_label = Label(editor, text="Créditos")
    credits_info = Text(editor, height=20, width=RIGHT_BOX_WIDTH, name="credits")
    credits_label.grid(row=4, column=2, sticky=S)
    credits_info.grid(row=5, column=2, sticky=N)
    return editor 