from tkinter import *
from tkinter.filedialog import *

# from tkFileDialog import *

fileName = None

def newFile():
    global filename
    filename = "Untitled"
    # text.delete(0.0,END)
    text.delete(0.0,END)

def saveFiel():
    global filename

    t = text.get(0.0,END)
    f = open(filename, 'w')
    f.write(t)
    f.close()
    pass

def saveAs():
    # f = asksaveasfile(mode = 'w',defaulttexttension = '.txt')
    f = asksaveasfile(mode='w',defaultextension = '.txt')
    t = text.get(0.0, END)

    try:
        f.write(t.rstrip())
    except:
        showerror(title = "Oops!",message = "Abilty'nt")

def openFilE():
    f = askopenfile(mode = 'r')
    t = f.read()
    text.delete(0.0 , END)
    text.insert(0.0,t)


root = Tk()
root.title("My text Editor")
root.minsize(width = 400,height=400)
root.maxsize(width = 600,height=600)


text = Text(root,width = 400 , height = 400)
text.pack()


menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label = "New",command = newFile)
filemenu.add_command(label = "Open",command = openFilE)
filemenu.add_command(label = "Save",command = saveFiel)
filemenu.add_command(label = "Save+as",command = openFilE)
filemenu.add_separator()
filemenu.add_command(label = "quit",command = root.quit)
menubar.add_cascade(label = "File" ,menu = filemenu)
root.config(menu = menubar )
root.mainloop()
