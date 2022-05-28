from interface import Interface
import tkinter as tk
import settings as s
from imgIO import read
from TP1 import  histogram
#mainWindow = tk.Tk()
#Interface(mainWindow)
#mainWindow.mainloop()



read("./input/mona.pgm")

print(histogram (s.image_orig))