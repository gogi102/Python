import tkinter

win = tkinter.Tk()

# Listbox 생성
listbox = tkinter.Listbox(win, width=10, height=5)
listbox.config(borderwidth=3)
# Listbox에 요소 추가하기
listbox.insert(0, '0번 Item');
listbox.insert(1, '1번 Item');
listbox.insert(2, '2번 Item');
listbox.insert(3, '3번 Item');
listbox.insert(4, '4번 Item');

# Listbox에 요소 삭제하기
listbox.delete(0);  # 0번 index 요소 삭제
listbox.delete(3, 4);
listbox.pack()

win.mainloop()
