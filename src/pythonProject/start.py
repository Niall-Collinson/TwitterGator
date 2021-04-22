import tkinter as tk
from PIL import ImageTk, Image
import requests
from gui import gui

HEIGHT = 500
WIDTH = 600

def start_function():
    root.destroy()
    gui()

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

path = "jungle.png"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(root, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.place(relwidth=1, relheight=1)

#Upper frame
upper_frame = tk.Frame(root, bg='#80c1ff', bd=5)
upper_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

label = tk.Label(upper_frame, text="TWITTER GATOR")
label.config(font=("Courier", 44))
label.place(relx=0, relwidth=1, relheight=1)

#Main frame
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.4, anchor='n')

label = tk.Label(frame, text="Twitter Gator tells you what people are talking about.\n\n"
                             "Made by Niall Collinson.")
label.place(relwidth=1, relheight=1)

#Lower frame
lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.8, relwidth=0.75, relheight=0.1, anchor='n')

button = tk.Button(lower_frame, text="START", font=40, command=lambda: start_function())
button.place(relheight=1, relwidth=1)

root.wm_title("Twitter Gator")
root.mainloop()