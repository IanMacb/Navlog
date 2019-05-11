from tkinter import *

root = Tk()
frame = Frame(bg='#7dbdc1')
frame.place(relheight=1.0, relwidth=1.0)

menuBar = Menu()
fileMenu = Menu(tearoff=0)
fileMenu.add_command(label="New", command='')
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)
menuBar.add_cascade(label="File", menu=fileMenu)
root.config(menu=menuBar)

inputFrame = Frame(frame, bg='#cedbe2')
inputFrame.place(height=40, relwidth=1.0)
entry1 = Entry(inputFrame)
entry1.place(anchor='w', relx=0.05, rely=0.5, relwidth=0.4)
entry2 = Entry(inputFrame)
entry2.place(anchor='e', relx=0.95, rely=0.5, relwidth=0.4)

buttonFrame = Frame(frame, bg='#6e8dd1')
buttonFrame.place(height=100, relwidth=1.0, y=40)
add = Button(buttonFrame, text='+', command='', padx=10)
add.place(anchor='n', relx=0.2, rely=0.1)
sub = Button(buttonFrame, text='-', command='', padx=10)
sub.place(anchor='n', relx=0.5, rely=0.1)
add = Button(buttonFrame, text='*', command='', padx=10)
add.place(anchor='n', relx=0.2, rely=0.5)
sub = Button(buttonFrame, text='/', command='', padx=10)
sub.place(anchor='n', relx=0.5, rely=0.5)

# button = Button(frame, text='Exit', command='exit', padx='10')
# button.pack(side='bottom')

root.mainloop()
