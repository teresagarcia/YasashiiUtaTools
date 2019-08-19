from tkinter import *
import sys
sys.path.append('src') 

translation_txt = sys.argv[1]
original_txt = sys.argv[2]

if __name__ == '__main__':
    editor = Tk()

    translation_board = Text(editor, height=50, width=100)
    translation_board.grid(row=0, column=0)
    editing_board = Text(editor, height=50, width=100)
    editing_board.grid(row=0, column=1)
    button = Button(editor, text="Enviar")
    button.grid(row = 1, column=0, columnspan=2)
    editor.mainloop()  

