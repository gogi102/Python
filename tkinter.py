from tkinter import *
from tkinter import messagebox
def clickButton():
    messagebox.showinfo("메시지 박스 제목","메시지 박스 내용")

a = Tk()

a.title("과학 과세특")

button1=Button(a, text="누르세요",fg="red",bg="yellow",command= clickButton)
button1.pack()

a.mainloop()

askyesno = input()

if askyesno("확인", "정말 삭제하시겠습니까?"):
    # Yes : 삭제진행
else:
    # No : 삭제안함
