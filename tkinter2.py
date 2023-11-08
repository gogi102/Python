import tkinter

win = tkinter.Tk()

label = tkinter.Label(win,
    text = 'label',
    background = 'white')

label.config(text = 'ㅎㅇㅎㅇ', width = 9, height = 2)
label.pack()

win.title('과학')
win.geometry('600x600+50+50')
win.resizable(False,True)
win.option_add('*Font','굴림 25')
win.mainloop()
