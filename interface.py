import settings as s
import TP3 as TP3
import imgIO as io
import TP2 as c
import stats as st
import TP1 as tp
import binary as b
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
import utils

matplotlib.use('TkAgg')
__author__ = 'Souheil'


class Interface:
    def __init__(self, window):
        self.window = window
        self.window.title('TP-ImageProcess')
        self.menu_initialisation()
        self.window.geometry(f'{self.window.winfo_screenwidth() - 100}x{self.window.winfo_screenheight() - 100}+10+10')
        self.currentimage = []
        self.previousimage = []

    def menu_initialisation(self):

        Frametools = tk.Frame(self.window, bg="#eeeeee",height=self.window.winfo_screenheight() * 0.2 ,)
        Frametools.pack_propagate(0)
        Frametools.pack(anchor=tk.N, side=tk.TOP, fill=tk.X, expand=tk.YES)

        FrameFile = tk.Frame(Frametools, height=100, width=50, padx=self.window.winfo_screenwidth()* 0.3)
        tk.Label(FrameFile, text="Image Path:").grid(row=0, column=0, padx=2)
        self.entry_text = tk.StringVar()
        self.entry_text.set("input/mona.pgm")
        tk.Entry(FrameFile, width=30, textvariable=self.entry_text).grid(row=1, column=0, padx=10)
        FrameFile.pack(anchor=tk.NW,side=tk.TOP)

        Frameopensave = tk.Frame(FrameFile, height=100, width=100, pady=5,padx=20)
        tk.Button(Frameopensave, text="Open",bg='#aeae54', fg="white", padx=10, pady=5, command=self.openButton_callback).grid(row=0, column=0,padx=10)
        tk.Button(Frameopensave, text="Local",bg='#aeae54', fg="white", padx=10, pady=5, command=self.local_equalisation_callback).grid(row=0, column=1,padx=10)
        tk.Button(Frameopensave, text="Save",bg='#aeae54', fg="white", padx=10, pady=5, command=self.saveButton_callback).grid(row=0, column=2,padx=10)
        self.original_button = tk.Button(Frameopensave, text="Original",bg='#aeae54', fg="white", state=tk.DISABLED, padx=10, pady=5, command=self.originalButton_callback)
        self.original_button.grid(row=0, column=2, padx=10)
        self.undo_button = tk.Button(Frameopensave, text="Undo",bg='#aeae54', fg="white", state=tk.DISABLED, padx=10, pady=5, command=self.undoButton_callback)
        self.undo_button.grid(row=0, column=3, padx=10)
        Frameopensave.grid(row=2 , column=0)

        ####################

        Framecontrast = tk.Frame(Frametools, height=100, width=200, padx=5)
        ttk.Label(Framecontrast, text="Contrast", width=15, background="#fff")
        tk.Button(Framecontrast, text="Equalisation ", bg='#234561', fg="white", width=15, padx=10, pady=5, command=self.equalisation_callback).grid(row=0, column=0)
        tk.Button(Framecontrast, text="Local Equalisation ", bg='#234561', fg="white", width=15, padx=10, pady=5, command=self.local_equalisation_callback).grid(row=0,  column=1)
        tk.Button(Framecontrast, text="Inverse", width=15, bg='#234561', fg="white", padx=10, pady=5, command=self.inverse_callback).grid(row=1, column=1)
        self.original_button = tk.Button(Framecontrast, width=15, text="Dark Dilatation",bg='#234561', fg="white", padx=10, pady=5, command=self.darkd_callback)
        self.original_button.grid(row=1, column=0, padx=10)
        self.undo_button = tk.Button(Frameopensave, text="Undo", bg='#234561', fg="white", state=tk.DISABLED, padx=10, pady=5, command=self.undoButton_callback)
        self.undo_button.grid(row=0, column=3, padx=10)
        Framecontrast.pack(anchor=tk.NW,side=tk.LEFT)
###################
        Framefilter = tk.Frame(Frametools, height=100, width=100, pady=5)
        ttk.Label(Framefilter, text="filters",width=15, background="#fff")
        tk.Button(Framefilter, text="Generate noise ", bg='#ac4561', fg="white",width=15, padx=10, pady=5, command=self.noise_callback).grid(row=0, column=0,padx=10)
        tk.Button(Framefilter, text="Average Filter ", bg='#ac4561', fg="white",width=15, padx=10, pady=5, command=self.average_callback).grid(row=0, column=1, padx=10)
        self.original_button = tk.Button(Framefilter, bg='#ac4561', fg="white",width=15, text="Mediane Filter", padx=10, pady=5, command=self.median_callback)
        tk.Button(Framefilter, text="Prewitt", bg='#ac4561', fg="white", padx=10, pady=5,width=15, command=self.prewitt_callback).grid(row=1, column=1, padx=10)
        self.original_button.grid(row=1, column=0, padx=10)
        Framefilter.pack(anchor=tk.NW,side=tk.LEFT)
##################

        Framesthresh = tk.Frame(Frametools, height=100, width=100, pady=5)
        tk.Button(Framesthresh, text="thresholding", bg='#45ae54', fg="white",width=15, padx=10, pady=5, command=self.thresholding_callback).grid(row=0,column=0,padx=10)
        tk.Button(Framesthresh, text="Manual thresholding", bg='#45ae54', fg="white",width=15, padx=10, pady=5, command=self.manualthresholding_callback).grid(row=0, column=1, padx=10)
        tk.Button(Framesthresh, text="Dilatation",width=15, bg='#45ae54', fg="white", padx=10, pady=5, command=self.dilatation_callback).grid(row=1, column=0, padx=10)
        tk.Button(Framesthresh, text="Closing",width=15, bg='#45ae54', fg="white", padx=10, pady=5, command=self.closing_callback).grid(row=0, column=2, padx=10)
        tk.Button(Framesthresh, text="Opening",width=15, bg='#45ae54', fg="white", padx=10, pady=5, command=self.opening_callback).grid(row=1, column=2, padx=10)
        self.original_button = tk.Button(Framesthresh,width=15,bg='#45ae54', fg="white", text="Erosion", padx=10, pady=5,command=self.median_callback)
        self.original_button.grid(row=1, column=1, padx=10)
        self.undo_button = tk.Button(Frameopensave, text="Undo", bg='#aeae54', fg="white", state=tk.DISABLED, padx=10, pady=5, command=self.undoButton_callback)
        self.undo_button.grid(row=0, column=3, padx=10)
        Framesthresh.pack(anchor=tk.NW,side=tk.LEFT)

##################
        self.imageframe = tk.Frame(self.window, width=self.window.winfo_screenwidth() * 0.4, height=self.window.winfo_screenheight() * 0.7)
        self.imageframe.pack_propagate(0)
        self.imageframe.pack(side=tk.LEFT, fill=tk.Y)
#################
        Framestats = tk.Frame(self.window, height=self.window.winfo_screenheight()* 0.7 , width=self.window.winfo_screenwidth() * 0.5)
        Framestats.pack_propagate(0)
        Framestats.pack(anchor=tk.N, side=tk.BOTTOM, fill=tk.Y, expand=tk.YES)
        FrameHistogram = tk.Frame(Framestats, width=self.window.winfo_screenwidth() * 0.3, height=self.window.winfo_screenheight() * 0.5, pady=5)
        tk.Label(FrameHistogram, text="Histogram:").pack(padx=10)
        self.fig2 = Figure(figsize=(6, 5), dpi=100)
        self.ax2 = self.fig2.add_subplot(111)
        canvas2 = FigureCanvasTkAgg(self.fig2, FrameHistogram)
        plot_widget2 = canvas2.get_tk_widget()
        plot_widget2.config(width=self.window.winfo_screenwidth() * 0.3,  height=self.window.winfo_screenheight() * 0.5)
        plot_widget2.pack(expand=tk.YES, anchor=tk.CENTER,  padx=5)
        FrameHistogram.pack_propagate(0)
        FrameHistogram.pack(anchor=tk.NW, side=tk.LEFT)

        Framethreshold = tk.Frame(Framestats, height=100, width=100,)
        tk.Label(Framethreshold, text="Manual threshold value: ").grid(row=0, column=0, padx=10)
        self.thresh_slider = tk.Scale(Framethreshold, from_=0, to=0, length=150, tickinterval=0, orient=tk.HORIZONTAL)
        self.thresh_slider.grid(row=0, column=2)
        Framethreshold.pack(anchor=tk.NW)
        ttk.Separator(Framestats, orient='horizontal').pack(fill='x', )

        Framesize = tk.Frame(Framestats, height=100, width=100, pady=5)
        self.size_num = tk.Spinbox(Framesize, width=3, from_=3, to=29, increment=2)
        self.size_num.grid(row=0, column=2)
        Framesize.pack(anchor=tk.NW, side=tk.LEFT)

        Framewidth = tk.Frame(Framestats, height=100, width=100, pady=5)
        tk.Label(Framewidth, text="Width:").grid(row=0, column=0, padx=10)
        self.width_text = tk.Label(Framewidth, text="0", width=15, relief=tk.SUNKEN)
        self.width_text.grid(row=0, column=2)
        Framewidth.pack(anchor=tk.NW)

        Frameheight = tk.Frame(Framestats, height=100, width=100, pady=5)
        tk.Label(Frameheight, text="Length:").grid(row=0, column=0, padx=10)
        self.height_text = tk.Label(Frameheight, text="0", width=15, relief=tk.SUNKEN)
        self.height_text.grid(row=0, column=2)
        Frameheight.pack(anchor=tk.NW)

        Framepixel = tk.Frame(Framestats, height=100, width=100, pady=5)
        tk.Label(Framepixel, text="Number of pixels:").grid(row=0, column=0, padx=10)
        self.pixel_text = tk.Label(Framepixel, text="0", width=15, relief=tk.SUNKEN)
        self.pixel_text.grid(row=0, column=2)
        Framepixel.pack(anchor=tk.NW)

        ttk.Separator(Framestats, orient='horizontal').pack(fill='x', pady=5)

        Frameaverage = tk.Frame(Framestats, height=100, width=100, pady=5)
        tk.Label(Frameaverage, text="Average:").grid(row=0, column=0, padx=10)
        self.average_text = tk.Label(Frameaverage, text="0", width=25, relief=tk.SUNKEN)
        self.average_text.grid(row=0, column=2)
        Frameaverage.pack(anchor=tk.NW)

        Framedeviation = tk.Frame(Framestats, height=100, width=100, pady=5)
        tk.Label(Framedeviation, text="Standard deviation:").grid(row=0, column=0, padx=10)
        self.deviation_text = tk.Label(Framedeviation, text="0", width=25, relief=tk.SUNKEN)
        self.deviation_text.grid(row=0, column=2)
        Framedeviation.pack(anchor=tk.NW)

        Frameentropy = tk.Frame(Framestats, height=100, width=100, pady=5)
        tk.Label(Frameentropy, text="Entropy:").grid(row=0, column=0, padx=10)
        self.entropy_text = tk.Label(Frameentropy, text="0", width=25, relief=tk.SUNKEN)
        self.entropy_text.grid(row=0, column=2)
        Frameentropy.pack(anchor=tk.NW)

        FrameSNR = tk.Frame(Framestats, height=100, width=100, pady=5)
        tk.Label(FrameSNR, text="SNR:").grid(row=0, column=0, padx=10)
        self.SNR_text = tk.Label(FrameSNR, text="0", width=25, relief=tk.SUNKEN)
        self.SNR_text.grid(row=0, column=2)
        FrameSNR.pack(anchor=tk.NW)

        FrameConsole = tk.Frame(Framestats, height=100, width=100, pady=5)
        tk.Label(FrameConsole, text="Console:").pack()
        self.console = tk.Text(FrameConsole, height=10, width=55, fg="green", bg="black")
        self.console.pack()
        FrameConsole.pack(anchor=tk.S, side=tk.BOTTOM)


        self.fig1 = Figure(figsize=(6, 5), dpi=100)
        self.ax1 = self.fig1.add_subplot(111)
        canvas1 = FigureCanvasTkAgg(self.fig1, self.imageframe)
        plot_widget = canvas1.get_tk_widget()
        plot_widget.config(width=self.window.winfo_screenwidth() * 0.4, height=self.window.winfo_screenheight())
        plot_widget.pack(expand=tk.YES, anchor=tk.CENTER, pady=20, padx=20)

    def updateStats(self):
        self.width_text.config(text=str(s.width))
        self.height_text.config(text=str(s.height))
        self.pixel_text.config(text=str(st.nbPixels()))
        self.average_text.config(text=str(tp.avg(self.currentimage)))
        self.deviation_text.config(text=str(tp.ecartype(self.currentimage)))
        self.entropy_text.config(text=str(st.entropy(self.currentimage)))
        self.SNR_text.config(text=str(st.SNR(self.currentimage)))
        self.displayHistogram()
        self.displayImage()

    def displayImage(self):
        self.ax1.clear()
        self.ax1.imshow(self.currentimage, cmap='gray')
        self.fig1.canvas.draw()

    def displayHistogram(self):
        self.ax2.clear()
        self.ax2.plot(tp.histogram(self.currentimage))
        self.fig2.canvas.draw()

    def openButton_callback(self):
        try:
            io.read(self.entry_text.get())
            self.original_button.config(state=tk.NORMAL)
            self.undo_button.config(state=tk.DISABLED)
            self.thresh_slider.config(to=s.graylevel,tickinterval=s.graylevel//4+1)
            self.thresh_slider.set(s.graylevel//2+1)
            self.currentimage = s.image_orig.copy()
            self.updateStats()
            self.writeConsole("New image opened.\n")
        except Exception:
            print(Exception.__traceback__)
            self.writeConsole('readError: error with ' + self.entry_text.get() + ': has wrong type or size.\n')
        except FileNotFoundError:
            self.writeConsole("File not found, try again.\n")

    def saveButton_callback(self):
        io.write(self.entry_text.get(), self.currentimage)
        self.writeConsole("Image saved.\n")

    def writeConsole(self, text):
        self.console.config(state=tk.NORMAL)
        self.console.insert(tk.END, text)
        self.console.config(state=tk.NORMAL)

    def originalButton_callback(self):
        self.previousimage = self.currentimage
        self.undo_button.config(state=tk.NORMAL)
        self.currentimage = s.image_orig.copy()
        self.updateStats()
        self.writeConsole("Reverted to original image.\n")

    def undoButton_callback(self):
        self.currentimage = self.previousimage
        self.undo_button.config(state=tk.DISABLED)
        self.updateStats()
        self.writeConsole("Undo to previous image.\n")

    def equalisation_callback(self):
        self.previousimage = self.currentimage
        self.undo_button.config(state=tk.NORMAL)
        self.currentimage = c.equalization(self.currentimage)
        self.updateStats()
        self.writeConsole("Equalisation applied.\n")

    def local_equalisation_callback(self):
        self.previousimage = self.currentimage
        self.undo_button.config(state=tk.NORMAL)
        self.currentimage = c.local_equalization(self.currentimage, int(self.size_num.get()))
        self.updateStats()
        self.writeConsole("Local equalisation applied.\n")

    def darkd_callback(self):
        self.previousimage = self.currentimage
        self.undo_button.config(state=tk.NORMAL)
        self.currentimage = c.dark_dilatation(self.currentimage)
        self.updateStats()
        self.writeConsole("Dark dilatation applied.\n")

    def lightd_callback(self):
        self.previousimage = self.currentimage
        self.undo_button.config(state=tk.NORMAL)
        self.currentimage = c.light_dilatation(self.currentimage)
        self.updateStats()
        self.writeConsole("Light dilatation applied.\n")

    def middled_callback(self):
        self.previousimage = self.currentimage
        self.undo_button.config(state=tk.NORMAL)
        self.currentimage = c.middle_dilatation(self.currentimage)
        self.updateStats()
        self.writeConsole("Middle dilatation applied.\n")

    def inverse_callback(self):
        self.previousimage = self.currentimage
        self.undo_button.config(state=tk.NORMAL)
        self.currentimage = c.inverse(self.currentimage)
        self.updateStats()
        self.writeConsole("Inversion applied.\n")


    def add_point_callback(self):
        x=self.entry_X.get()
        y=self.entry_Y.get()
        if (x not in range(0,s.graylevel+1) or y not in range(0,s.graylevel+1)):
            return
        self.points.append([x,y])
        self.points.sort()
        pointX=[x[0] for x in self.points]
        pointY=[y[1] for y in self.points]
        self.ax3.clear()
        self.ax3.set_xlim([0,s.graylevel])
        self.ax3.set_ylim([0, s.graylevel])
        self.ax3.plot(pointX,pointY,color='red', marker='o')
        self.ax3.grid(True)
        self.fig3.canvas.draw()



    def median_callback(self):
        self.previousimage = self.currentimage
        self.undo_button.config(state=tk.NORMAL)
        self.currentimage = TP3.filter_median(self.currentimage, int(self.size_num.get()))
        self.updateStats()
        self.writeConsole("Median filter applied.\n")

    def average_callback(self):
        self.previousimage = self.currentimage
        self.undo_button.config(state=tk.NORMAL)
        self.currentimage = TP3.filter_average(self.currentimage, int(self.size_num.get()))
        self.updateStats()
        self.writeConsole("Average filter applied.\n")

    def gaussian_callback(self):
        self.previousimage = self.currentimage
        self.undo_button.config(state=tk.NORMAL)
        self.currentimage = TP3.filter_gauss(self.currentimage, int(self.size_num.get()))
        self.updateStats()
        self.writeConsole("Gaussian filter applied.\n")

    def high_boost_callback(self):
        self.previousimage = self.currentimage
        self.undo_button.config(state=tk.NORMAL)
        self.currentimage = TP3.filter_highboost(self.currentimage, int(self.size_num.get()))
        self.updateStats()
        self.writeConsole("High boost filter applied.\n")

    def laplace_callback(self):
        self.previousimage = self.currentimage
        self.undo_button.config(state=tk.NORMAL)
        self.currentimage = TP3.filter_laplace(self.currentimage)
        self.updateStats()
        self.writeConsole("Laplace filter applied.\n")

    def prewitt_callback(self):
        self.previousimage = self.currentimage
        self.undo_button.config(state=tk.NORMAL)
        self.currentimage = TP3.filter_prewitt(self.currentimage, int(self.size_num.get()))
        self.updateStats()
        self.writeConsole("Prewitt filter applied.\n")

    def manualthresholding_callback(self):
        self.previousimage = self.currentimage
        self.undo_button.config(state=tk.NORMAL)
        self.currentimage = b.binarize(self.currentimage,self.thresh_slider.get())
        self.updateStats()
        self.writeConsole("Manual thresholding applied.\n")

    def thresholding_callback(self):
        self.previousimage = self.currentimage
        self.undo_button.config(state=tk.NORMAL)
        self.currentimage,thmin = b.thresholding(self.currentimage)
        self.thresh_slider.set(thmin)
        self.updateStats()
        self.writeConsole(f"Thresholding applied with the threshold: {thmin}.\n")

    def dilatation_callback(self):
        self.previousimage = self.currentimage
        self.undo_button.config(state=tk.NORMAL)
        self.currentimage = b.dilatation(self.currentimage, int(self.size_num.get()))
        self.updateStats()
        self.writeConsole("Dilatation applied.\n")

    def erosion_callback(self):
        self.previousimage = self.currentimage
        self.undo_button.config(state=tk.NORMAL)
        self.currentimage = b.erosion(self.currentimage, int(self.size_num.get()))
        self.updateStats()
        self.writeConsole("Erosion applied.\n")

    def closing_callback(self):
        self.previousimage = self.currentimage
        self.undo_button.config(state=tk.NORMAL)
        self.currentimage = b.closing(self.currentimage, int(self.size_num.get()))
        self.updateStats()
        self.writeConsole("Closing applied.\n")

    def opening_callback(self):
        self.previousimage = self.currentimage
        self.undo_button.config(state=tk.NORMAL)
        self.currentimage = b.opening(self.currentimage, int(self.size_num.get()))
        self.updateStats()
        self.writeConsole("Opening applied.\n")

    def noise_callback(self):
        self.previousimage = self.currentimage
        self.undo_button.config(state=tk.NORMAL)
        self.currentimage = TP3.noise(self.currentimage, s.width, s.height, s.graylevel)
        self.updateStats()
        self.writeConsole("Noise applied.\n")

    def ascii_callback(self):
        asciiimage = utils.ascii(self.currentimage, s.width, s.height)
        io.write("output\\ascii.txt", asciiimage)
        self.writeConsole("ascii.txt saved in output folder.\n")

    def QuitMenuButton_callback(self):
        self.window.destroy()


