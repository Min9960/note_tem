from tkinter import *
from tkinter.filedialog import *

# 새창열기
def new_file():
    text_area.delete(1.0,END)

# 현재창 저장하기
def save_file():
    f = asksaveasfile(mode = "w", defaultextension=".txt",filetypes=[('Text files', '.txt')])
    text_save = str(text_area.get(1.0, END))
    f.write(text_save)
    f.close()

# 정보 팝업
maker_name = ""
def save_maker():
    def save():
        global maker_name
        maker_name = entry.get()
        popup.destroy()
    popup = Toplevel(window)
    popup.title("만든이 저장")
    popup.geometry("250x80")
    Label(popup, text="만든이 이름:").pack()
    entry = Entry(popup)
    entry.pack()
    Button(popup, text="저장", command=save).pack()

def maker():
    help_view = Toplevel(window)
    help_view.geometry("300x50")
    help_view.title("만든이")
    if maker_name == "":
        text = "만든이가 설정되지 않았습니다."
    else:
        text = f"{maker_name}(이)가 만든 메모장입니다."
    lb = Label(help_view, text=text)
    lb.pack()

window = Tk()
window.title("Notepad")
window.geometry("400x400")
window.resizable(False, False)

menu = Menu(window)
menu_1 = Menu(menu, tearoff=0)
menu_1.add_command(label="새파일", command=new_file)
menu_1.add_command(label="저장", command=save_file)
menu_1.add_separator()
menu_1.add_command(label="종료", command=window.destroy)
menu.add_cascade(label="파일", menu=menu_1)

menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label="만든이 저장", command=save_maker)
menu_2.add_command(label="만든이", command=maker)
menu.add_cascade(label="만든이", menu=menu_2)

text_area = Text(window)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky = N + E + S + W)

window.config(menu=menu)

window.mainloop()