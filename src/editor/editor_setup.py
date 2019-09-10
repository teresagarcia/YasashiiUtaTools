from tkinter import *

def set_layout():
    editor = Tk()

    title_label = Label(editor, text="Título")
    title_label.grid(row=0, column=0)
    
    title = Entry(editor, width=55, name="title")
    title.grid(row=0, column=0, columnspan=2)

    translation_board = Text(editor, height=55, width=80)
    translation_board.grid(row=2, column=0, rowspan=5)

    editing_board = Text(editor, height=55, width=80)
    editing_board.grid(row=2, column=1, rowspan=5)

    button = Button(editor, text="Enviar")
    button.grid(row=7, column=0, columnspan=2)

    tags_label = Label(editor, text="Etiquetas")
    tags = Text(editor, height=10, width=35)
    tags_label.grid(row=2, column=2, sticky=S)
    tags.grid(row=3, column=2, sticky=N)

    credits_label = Label(editor, text="Créditos")
    credits_info = Text(editor, height=20, width=35)
    credits_label.grid(row=4, column=2, sticky=S)
    credits_info.grid(row=5, column=2, sticky=N)
    return editor