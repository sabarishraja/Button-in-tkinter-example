import tkinter

window = tkinter.Tk()
window.title("My program")
window.minsize(width=500, height=300)
label = tkinter.Label(text="TRY TO CHANGE ME")
label.pack()


def click():
    label.config(text="Congrats! You changed me")


button = tkinter.Button(text="PRESS ME DUDE!!!", command=click)
button.pack()

