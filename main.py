from matplotlib import pyplot as plt

from interface import Interface
import tkinter as tk
import settings as s
from imgIO import read
from TP1 import  histogram
import TP1

mainWindow = tk.Tk()
Interface(mainWindow)
mainWindow.mainloop()

  #  read("./input/mona.pgm")
  #  plt.imshow(s.image_orig,cmap='gray')
  #  print(s.image_orig)
