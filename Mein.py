from tkinter import *
from ClasSic import *
# --------------------
from tkinter.messagebox import showinfo
# --------------------
import ClasSic
#-------------------------------------------------------------------------
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
#-------------------------------------------------------------------------
def open_info():
    showinfo(title='Гайд', message='И так, всё просто, не доводи растения до крайностей: \n 1) Не доводи статусы Влаги и света до -10 и +60 \n 2) Следи за статусом! Он подскажет на сколько всё плохо \n 3) Расходы меняются в зависимости от времени суток \n 4) И да, пока ты читал это ты проиграл, начинай заново')
#-------------------------------------------------------------------------
root = Tk()
root.title('Plants not VS Davit')
root.geometry('600x250')
root.config(bg='lightblue')
root.resizable(False, False)
#root.iconbitmap(default="favicon.ico")
root.protocol('WM_DELETE_WINDOW')
#-------------------------------------------------------------------------
info_button = Button(text='Информация', command=open_info)
info_button.place(x = 498, y = 14)
#-------------------------------------------------------------------------
Bt1 = Button(text = f'Лейка', command = Watering)
Bt1.place(x = 20, y = 210)
#----------------------
Bt2 = Button(text = f'Совок' , command = Dig)
Bt2.place(x = 80, y = 210)
#----------------------
Bt3 = Button(text = f'Компостер {ClasSic.Удобрение}' , command = Fertilizer)
Bt3.place(x = 140, y = 210)
#----------------------
Bt5 = Button(text = f'Открыть шторы' , command = Curtains)
Bt5.place(x = 235, y = 210)
#----------------------
Bt4 = Button(text = f'Пополнить лейку' , command = Weather_Add)
Bt4.place(x = 475, y = 210)
#-------------------------------------------------------------------------
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
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
if __name__ == "__main__":
    T.start()
    root.mainloop()