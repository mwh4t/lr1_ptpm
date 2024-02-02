from tkinter import *
from tkmacosx import Button
from other.params import BTN_CONFIG, TEXT_CONFIG


def x_questions_btn_func(root):
    """
    Функция для вопросов по х
    """
    def ok_btn_func():
        """
        Функция кнопки "ОК"
        """
        top.destroy()

    top = Toplevel(root)
    top.title("Вопросы по х")
    top.geometry("+520+350")
    top.resizable(False, False)
    top.configure(bg="#262626")

    # установка top как дочернего окна root
    top.transient(root)

    lbl = Label(top, text="x∈(−∞,−2)∪(−2,0)∪(0,2)∪(2,+∞), x≠−2,2",
                **TEXT_CONFIG)
    lbl.pack(padx=8, pady=8)

    # кнопка "далее"
    next_btn = Button(top, text="ОК", **BTN_CONFIG,
                      command=lambda: ok_btn_func())
    next_btn.pack(side=TOP, padx=8, pady=8)

    # установка фокуса на top
    top.grab_set()
    # ожидание закрытия top
    root.wait_window(top)
    # после закрытия top освобождение фокуса
    root.grab_release()
