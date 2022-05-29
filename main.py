from matplotlib import pyplot as plt
from tkinter import ttk
from interface import Interface
from ttkthemes import ThemedStyle
import tkinter as tk
import settings as s
from imgIO import read
from TP1 import  histogram
import TP1
from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedStyle


mainWindow = tk.Tk()
mainWindow.style = ThemedStyle(mainWindow)
mainWindow.style.theme_use("equilux")
mainWindow.style.configure("TLabel", background="black")
Interface(mainWindow)
mainWindow.mainloop()

  #  read("./input/mona.pgm")
  #  plt.imshow(s.image_orig,cmap='gray')
  #  print(s.image_orig)
