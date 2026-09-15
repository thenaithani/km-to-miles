import tkinter

window = tkinter.Tk()
window.title("km-miles converter")
window.minsize(400, 300)
window.maxsize(800, 600)

tittle = tkinter.Label(text="km-miles converter", font=("courier", 25))
tittle.place(x=50)

current_select = tkinter.Label(text="current conversion - NONE", font=("courier", 10))
current_select.place(x=50, y=50)

def conversion(event):
    chosen = change_convert.get(change_convert.curselection())
    if chosen == "km":
        current_select.config(text="current conversion - Km")
    if chosen == "Miles":
        current_select.config(text="current conversion - Miles")

attribute = tkinter.IntVar()
change_convert = tkinter.Listbox(height=2)
options = ["km", "Miles"]
for i in options:
    change_convert.insert(options.index(i), i)
change_convert.bind("<<ListboxSelect>>", conversion)
change_convert.place(x=150,y=100)


box = tkinter.Entry()
box.place(x=150, y=150)

window.mainloop()
