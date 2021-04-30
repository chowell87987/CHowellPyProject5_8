import tkinter as tk
import tkinter.font as tkFont

app = tk.Tk()
app.winfo_toplevel().title("Python GUI Project")
app.geometry("640x480")

fontStyle = tkFont.Font(family="Times New Roman", size=18)

labelExample = tk.Label(app, text="The system is idle.", font=fontStyle)

def SystemOn():
    labelExample.config(text = "System Running")

def SystemOff():
    labelExample.config(text = "System Off")

pixelVirtual = tk.PhotoImage(width=1, height=1)

labelExample.pack(side=tk.TOP)

button1 = tk.Button(app, text="System On", bg="gray", fg="black", image=pixelVirtual, width=200, height=100, compound="c", command = SystemOn)
button1.place(x=100, y=400)

button2 = tk.Button(app, text="System Off", bg="gray", fg="black", image=pixelVirtual, width=200, height=100, compound="c", command = SystemOff)
button2.place(x=340, y=400)

button3 = tk.Button(app, text="EXIT", command = app.quit)
button3.pack(side=tk.BOTTOM)

app.mainloop()