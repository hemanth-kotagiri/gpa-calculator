import tkinter as tk

HEIGHT = 700
WIDTH = 800


theWindow = tk.Tk()

canvas = tk.Canvas(theWindow,height=HEIGHT,width=WIDTH)
canvas.pack()

button = tk.Button(theWindow, text='Test')
button.pack()

theWindow.mainloop()
