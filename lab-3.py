import tkinter as tk
import random


def code_gen():
    letter_list = 'abcdefghijklmnopqrstuvwxyz'.upper()
    num_list = '0123456789'
    code = ''
    ind_num = []

    for i in range(4):
        ind_num.append(random.randint(0, 3) + i * 4 + i)  #Выбираем позиции на который будут цифры

    for i in range(19):
        if i in [4, 9, 14]:
            code += '-'
        elif i in ind_num:
            code += random.choice(num_list)
        else:
            code += random.choice(letter_list)

    code_lbl.configure(text=code)


window = tk.Tk()
bg_img = tk.PhotoImage(file='art.png')  #Фон
window.geometry('1200x675')
label_bg = tk.Label(window, image=bg_img)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

code_lbl = tk.Label(window, text='Your code')  #Поле с кодом
code_lbl.place(relx=0.5, rely=0.6, relwidth=0.3, anchor='s')

btn_gen = tk.Button(window, text='Generate code', width=20, command=lambda: code_gen())  #Кнопка для генерации кода
btn_gen.place(relx=0.5, rely=0.5, anchor='s')

window.mainloop()
