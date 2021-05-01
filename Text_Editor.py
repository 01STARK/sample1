from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('Text Editor')
#root.iconbitmap('C:\Users\rishiraj\Desktop\icon.ico')
root.geometry("900x450")


my_frame = Frame(root)
my_frame.pack(pady=2)


text_scroll= Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

my_text = Text(my_frame, width=97, height=25, font=("Helvetica,16"),selectbackground="Yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()


text_scroll.config(command=my_text.yview)





def newfile():
    global filename
    filename = "Untitled"
    text.delete(0.0,END)

def saveas():
    print("saving file")
    f = filedialog.asksaveAsfile(mode="w",defaultextextension='.txt')
    t = text.get(0.0,END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Oops!",message="Unable to Save File...:(")

def openfile():
    print("opening file")
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0,END)
    text.insert(0.0,t)
    current_openfile = f.name


def savefile():
    print("saving file")
    global filename
    t = text.get(0.0,END)
    f = open(current_openfile,'w')
    f.write(t)
    f.close()



menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command=newfile)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_command(label="Save",command=savefile)
#filemenu.add_command(label="Save As",command=saveas)
filemenu.add_command(label="Quit",command=root.destroy)
menubar.add_cascade(label="File",menu=filemenu)

root.config(menu=menubar)


root.mainloop()