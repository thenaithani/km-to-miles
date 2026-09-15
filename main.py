import tkinter

window = tkinter.Tk()
window.title("km-miles converter")
window.minsize(400, 300)
window.maxsize(800, 600)

tittle = tkinter.Label(text="km-miles converter", font=("courier", 25))
tittle.place(x=50)



box = tkinter.Entry()
box.place(x=150, y=150)

window.mainloop()
