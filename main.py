import tkinter

window = tkinter.Tk()
window.title("km-miles converter")
window.minsize(400, 300)
window.maxsize(800, 600)

tittle = tkinter.Label(text="km-miles converter", font=("courier", 25))
tittle.place(x=50)

current_select = tkinter.Label(text="current conversion - NONE", font=("courier", 10))
current_select.place(x=50, y=50)

km = False
Miles = False

def conversion(event):
    global km
    global Miles

    chosen = change_convert.get(change_convert.curselection())
    if chosen == "km":
        km = True
        Miles = False
        current_select.config(text="current conversion - Km-miles")
    if chosen == "Miles":
        Miles = True
        km = False
        current_select.config(text="current conversion - Miles-km")
answer = tkinter.Label(text="", font=("courier", 25))
answer.place(x=30, y=220)

def final_convert():
    global km
    global Miles
    if km:
        to_change = box.get()
        new_value = int(to_change) * 0.62

        answer.config(text=f"converted {new_value} miles")
    if Miles:
        to_change = box.get()
        new_value = int(to_change) * 1.60

        answer.config(text=f"converted {new_value} km")

convert = tkinter.Button(text="convert", command=final_convert)
convert.place(x=180, y=180)

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
