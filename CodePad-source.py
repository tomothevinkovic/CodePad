import msvcrt
import os
from tkinter import*
from tkinter.font import Font
from tkinter import filedialog

os.makedirs("C:\CodePad Documents", exist_ok=True)

print("Do not close this window, however, you can minimize it.")

window = Tk()
window.title("CodePad")
window.minsize(1366,768)
window.resizable(width=False, height=False)
window.configure(bg="#FFFFFF")
window.iconbitmap(r'CodePad.ico')
                    
                    

#Spremanje teksta
def SaveAsTxt():
    window.filename = filedialog.asksaveasfilename( filetypes = ( ("Text files", ".txt"), ("All files", ".") ) )
    f = ("%s.txt" %window.filename)
    try:
        fp = open(f)
    except IOError:
        fp = open(f, 'w+')
    
    inputValue = textbox.get("1.0", "end-1c")
    fp.write(inputValue)
    fp.close()

def SaveAsHtml():
    window.filename = filedialog.asksaveasfilename( filetypes = ( ("Text files", ".txt"), ("All files", ".") ) )
    f = ("%s.html" %window.filename)
    try:
        fp = open(f)
    except IOError:
        fp = open(f, 'w+')
    
    inputValue = textbox.get("1.0", "end-1c")
    fp.write(inputValue)
    fp.close()

#Otvaranje fajlova


def fileopen():
    openwindow = Tk()
    openwindow.title("Open a file")
    openwindow.minsize(300,100)
    openwindow.resizable(width=False, height=False)
    openwindow.configure(bg="#FFFFFF")

    def open_a_file():
        openwindow.filename = filedialog.askopenfilename( filetypes = ( ("Text files", ".txt"), ("Html files", ".html") ) )
        file = open(openwindow.filename)
        copy_value = file.read(10000000)
        textbox.insert(END, copy_value)
        openwindow.destroy()

    start = Button(openwindow, text="Open", command=open_a_file)
    start.place(x=10, y=150, width=70, height=25)

#MenuBar
menuBar = Menu(window)

#File
filemenu = Menu(window)
saveasmenu = Menu(window)#Save As
openmenu = Menu(window)#Save As
saveasmenu.add_radiobutton(label=".txt", command=SaveAsTxt)#Save as txt
saveasmenu.add_radiobutton(label=".html", command=SaveAsHtml)#Save as html
menuBar.add_cascade(label="File", menu=filemenu)
filemenu.add_cascade(label="Save As", menu=saveasmenu)
filemenu.add_radiobutton(label="Open", command=fileopen)
window.config(menu=menuBar)

#TextBox
textbox = Text(window)
textbox.place(x=10, y=10, width=1346, height=730)
myFont = Font(family="times new roman", size=12)
textbox.configure(font=myFont)
textbox.configure(bg="#FFFFFF")
textbox.configure(borderwidth="1")



#Font define
def Arial():
    myFont = Font(family="Arial", size=11)
    textbox.configure(font=myFont)

def TimesNewRoman():
    myFont = Font(family="Times New Roman", size=11)
    textbox.configure(font=myFont)

def Calibri():
    myFont = Font(family="Calibri", size=11)
    textbox.configure(font=myFont)

def Corbel():
    myFont = Font(family="Corbel", size=11)
    textbox.configure(font=myFont)

#Fontsize define
def size11():
    myFont = Font(size=11)
    textbox.configure(font=myFont)

def size12():
    myFont = Font(size=12)
    textbox.configure(font=myFont)

def size13():
    myFont = Font(size=13)
    textbox.configure(font=myFont)

def size14():
    myFont = Font(size=14)
    textbox.configure(font=myFont)

def size15():
    myFont = Font(size=15)
    textbox.configure(font=myFont)

def size16():
    myFont = Font(size=16)
    textbox.configure(font=myFont)

def size17():
    myFont = Font(size=17)
    textbox.configure(font=myFont)

def size18():
    myFont = Font(size=18)
    textbox.configure(font=myFont)

def size19():
    myFont = Font(size=19)
    textbox.configure(font=myFont)

def size20():
    myFont = Font(size=20)
    textbox.configure(font=myFont)

#Color define
def black():
    textbox.configure(foreground="black")
    textbox.config(insertbackground="black")

def white():
    textbox.configure(foreground="white")
    textbox.config(insertbackground="white")

def red():
    textbox.configure(foreground="red")
    textbox.config(insertbackground="red")

def orange():
    textbox.configure(foreground="orange")
    textbox.config(insertbackground="orange")

def green():
    textbox.configure(foreground="#5FFF54")
    textbox.config(insertbackground="#5FFF54")

def yellow():
    textbox.configure(foreground="yellow")
    textbox.config(insertbackground="yellow")

#Bg-color define
def bgwhite():
    textbox.configure(bg="#EEEEEE")

def bgblack():
    textbox.configure(bg="black")

def bggrey():
    textbox.configure(bg="#5A868E")
    
    

#Style
stylemenu = Menu(window)#Style
fontmenu = Menu(window)#Font
fontsizemenu = Menu(window)#FontSize
fontcolormenu = Menu(window)#FontColor
textbgmenu = Menu(window)#TextBackground
boldcursivemenu = Menu(window)#Boldcursive
menuBar.add_cascade(label="Style", menu=stylemenu)

#Font
stylemenu.add_cascade(label="Font", menu=fontmenu)
fontmenu.add_radiobutton(label="Arial", command=Arial)
fontmenu.add_radiobutton(label="Times New Roman", command=TimesNewRoman)
fontmenu.add_radiobutton(label="Calibri", command=Calibri)
fontmenu.add_radiobutton(label="Corbel", command=Corbel)

#FontSize
stylemenu.add_cascade(label="Font Size", menu=fontsizemenu)
fontsizemenu.add_radiobutton(label="11", command=size11)
fontsizemenu.add_radiobutton(label="12", command=size12)
fontsizemenu.add_radiobutton(label="13", command=size13)
fontsizemenu.add_radiobutton(label="14", command=size14)
fontsizemenu.add_radiobutton(label="15", command=size15)
fontsizemenu.add_radiobutton(label="16", command=size16)
fontsizemenu.add_radiobutton(label="17", command=size17)
fontsizemenu.add_radiobutton(label="18", command=size18)
fontsizemenu.add_radiobutton(label="19", command=size19)
fontsizemenu.add_radiobutton(label="20", command=size20)

#FontColor
stylemenu.add_cascade(label="Font Color", menu=fontcolormenu)
fontcolormenu.add_radiobutton(label="Black", command=black)
fontcolormenu.add_radiobutton(label="White", command=white)
fontcolormenu.add_radiobutton(label="Red", command=red)
fontcolormenu.add_radiobutton(label="Orange", command=orange)
fontcolormenu.add_radiobutton(label="Green", command=green)
fontcolormenu.add_radiobutton(label="Yellow", command=yellow)

#TextBackground
stylemenu.add_cascade(label="Background Color", menu=textbgmenu)
textbgmenu.add_radiobutton(label="Greyish-White", command=bgwhite)
textbgmenu.add_radiobutton(label="Black", command=bgblack)
textbgmenu.add_radiobutton(label="Greyish-Blue", command=bggrey)

htmlmenu = Menu(window)#HTML tagovi
basichtml = Menu(window)#Osnovni HTML tagovi
styling = Menu(window)#HTML tagovi za stil
fileimports = Menu(window)#HTML tagovi za umetanje fileova
organization = Menu(window)#HTML tagovi za organizaciju sajta
menuBar.add_cascade(label="HTML tags", menu=htmlmenu)

#HTML define
def html():
    textbox.insert(END, '<html>')
    
def head():
    textbox.insert(END, '<head>')
    
def body():
    textbox.insert(END, '<body>')

def paragraph():
    textbox.insert(END, '<p>')

def header():
    textbox.insert(END, '<h1>')

def italic():
    textbox.insert(END, '<i>')

def bold():
    textbox.insert(END, '<b>')

def link():
    textbox.insert(END, '<a>')

def image():
    textbox.insert(END, '<img src="">')

def div():
    textbox.insert(END, '<div>')

#HTML tagovi
htmlmenu.add_cascade(label="Basic", menu=basichtml)
htmlmenu.add_cascade(label="Text Styiling", menu=styling)
htmlmenu.add_cascade(label="File Importing", menu=fileimports)
htmlmenu.add_cascade(label="Website Organization", menu=organization)

basichtml.add_radiobutton(label="<html>", command=html)
basichtml.add_radiobutton(label="<head>", command=head)
basichtml.add_radiobutton(label="<body>", command=body)
styling.add_radiobutton(label="<p>", command=paragraph)
styling.add_radiobutton(label="<h1>", command=header)
styling.add_radiobutton(label="<i>", command=italic)
styling.add_radiobutton(label="<b>", command=bold)
styling.add_radiobutton(label="<a>", command=link)
fileimports.add_radiobutton(label="<img>", command=image)
organization.add_radiobutton(label="<div>", command=div)

#Undo,redo

def clear():
        textbox.delete("end-11c", "end-1c")

editmenu = Menu(window)
menuBar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_radiobutton(label="Undo", command=clear)

window.mainloop()

