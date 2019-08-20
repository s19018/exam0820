from tkinter import *
import tkinter.messagebox as mb

class App(Frame):
    def main(roman):
        num = 0
        r_n = {
            'a': 2,
            'b': 4,
            'c': 6,
            'd': 8,
            'e': 10,
            'f': 12,
            'g': 14,
            'h': 16,
            'i': 18,
            'j': 20,
            'k': 22,
            'l': 24,
            'm': 26,
            'n': 28,
            'o': 30,
            'p': 32,
            'q': 34,
            'r': 36,
            's': 38,
            't': 40,
            'u': 42,
            'v': 44,
            'w': 46,
            'x': 48,
            'y': 50,
            'z': 52,
        }
        pre = 0
        for i in range(len(roman) - 1, -1, -1):
            c = roman[i]
            n = r_n[c]
            if n >= pre:
                num += n
            else:
                num -= n
        return num

    def calc():
        name1 = txt.get()
        name2 = txt2.get()
        pro1 = App.main(name1)
        pro2 = App.main(name2)
        add = pro1 + pro2
        if add >= 100:
            while add >= 100:
                add = add / 2
            mb.showinfo("結果", "二人の相性は{}%です".format(add))
        else:
            mb.showinfo("結果", "二人の相性は{}%です".format(add))


root = Tk()

root.geometry('400x200')

root.title('名前相性占い')

lbl = Label(text='ローマ字で打って')
lbl.place(x=155, y=10)
lbl2 = Label(text='name')
lbl2.place(x=178, y=70)

txt = Entry(width=20)
txt.place(x=5, y=70)
txt2 = Entry(width=20)
txt2.place(x=225, y=70)


btn = Button(
    root,
    text="発表",
    command=App.calc,
)
btn.place(x=170, y=150)


root.mainloop()
