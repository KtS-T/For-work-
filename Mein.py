from tkinter import *
from ClasSic import *
# --------------------
from tkinter.messagebox import showinfo
import tkinter as tk
# --------------------
import ClasSic
# -------------------------------------------------------------------------
def Weather_Add():
    ClasSic.Stat.Долить_2()
def Watering():
    ClasSic.Stat.Полить()
def Dig():
    ClasSic.Stat.Вскопать()
def Fertilizer():
    ClasSic.Stat.Удобрить()
def Curtains():
    ClasSic.Stat.Осветить()
# -------------------------------------------------------------------------
def open_info():
    showinfo(title='Гайд', message='И так, всё просто, не доводи растения до крайностей: \n 1) Не доводи статусы Влаги и света до -10 и +60 \n 2) Следи за статусом! Он подскажет на сколько всё плохо \n 3) Расходы меняются в зависимости от времени суток \n 4) Можешь даже не пробовать тыкаться в [Совок] и [ПЭ] \n 5) И да, пока ты читал это ты проиграл, начинай заново')
# -------------------------------------------------------------------------
root = Tk()
root.title('Plants not VS Davit')
root.geometry('600x250')
root.config(bg='lightblue')
root.resizable(False, False)
#root.iconbitmap(default="favicon.ico")
root.protocol('WM_DELETE_WINDOW')
# -------------------------------------------------------------------------
info_button = Button(text='Информация', command=open_info)
info_button.place(x = 498, y = 14)
# -------------------------------------------------------------------------
Bt1 = Button(text = f'Лейка', command = Watering)
Bt1.place(x = 20, y = 210)
# ----------------------
Bt2 = Button(text = f'Совок' , command = Dig)
Bt2.place(x = 80, y = 210)
# ----------------------
Bt3 = Button(text = f'Компостер {ClasSic.Удобрение}' , command = Fertilizer)
Bt3.place(x = 140, y = 210)
# ----------------------
Bt5 = Button(text = f'Открыть шторы' , command = Curtains)
Bt5.place(x = 235, y = 210)
# ----------------------
Bt4 = Button(text = f'Пополнить лейку' , command = Weather_Add)
Bt4.place(x = 475, y = 210)
# -------------------------------------------------------------------------
Lb1 = Label(text = f'Влажность:')
Lb1.place(x = 20, y = 20)

Lb2 = Label(text = f'Освещённость:')
Lb2.place(x = 20, y = 60)

Lb3 = Label(text = f'ПЭ:')
Lb3.place(x = 20, y = 100)

Lb4 = Label(text = f'В Лейке : {ClasSic.Лейка} литров')
Lb4.place(x = 20, y = 167)

Lb5 = Label(text = f'Статус: Всё вроде ок', fg='black')
Lb5.place(x = 345, y = 212)

Lb6 = Label(text = f'Время: {ClasSic.Ttime}')
Lb6.place(x = 275, y = 15)
# -------------------------------------------------------------------------
canvas = tk.Canvas(root, width=600, height=250, highlightthickness=0)
canvas.place(x=0, y=0)
# -------------------------------------------------------------------------
images = {
    'небо_у': tk.PhotoImage(file="небо_утро.png", master=root),
    'небо_д': tk.PhotoImage(file="небо_день.png", master=root),
    'небо_в': tk.PhotoImage(file="небо_вечер.png", master=root),
    'небо_н': tk.PhotoImage(file="небо_ночь.png", master=root),
    'растение_ок': tk.PhotoImage(file="Растение(ок).png", master=root),
    'растение_норм': tk.PhotoImage(file="Растение(норм).png", master=root),
    'растение_дед': tk.PhotoImage(file="Растение(брух).png", master=root),
    'стены_д': tk.PhotoImage(file="стены_день.png", master=root),
    'стены_с': tk.PhotoImage(file="стены_вечер.png", master=root),
    'стены_н': tk.PhotoImage(file="стены_ночь.png", master=root),
    'Шторы_о': tk.PhotoImage(file="шторы открыты.png", master=root),
    'Шторы_з': tk.PhotoImage(file="шторы закрыты.png", master=root),
    'Оконная рама': tk.PhotoImage(file="оконная рама.png", master=root),
    'Стол': tk.PhotoImage(file="стол.png", master=root),
}
# -------------------------------------------------------------------------
sky = canvas.create_image(300,125, image=images['небо_у'], anchor='center')
# -------------------------------
wall = canvas.create_image(300, 125, image=images['стены_с'], anchor='center')
# -------------------------------
table = canvas.create_image(300, 125, image=images['Стол'], anchor='center')
# -------------------------------
window = canvas.create_image(300,125, image=images['Оконная рама'], anchor='center')
# -------------------------------
curtains = canvas.create_image(300, 125, image=images['Шторы_о'], anchor='center')
# -------------------------------
plant = canvas.create_image(300, 125, image=images['растение_ок'], anchor='center')
# -------------------------------------------------------------------------
# ------------------
def redraw():
    ClasSic.Stat.Uqdate_V()
    root.after(500, redraw)
# -------------------------------------------------------------------------
if __name__ == "__main__":
    ClasSic.Stat.set_graphics(canvas, images, sky, wall, plant, curtains)
    T.start()
    redraw()
    root.mainloop()