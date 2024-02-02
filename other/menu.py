from tkinter import *
from tkmacosx import Button, CircleButton
from other.params import (BTN_CONFIG, CIRCLE_BTN_CONFIG, TEXT_CONFIG,
                          EXP_CONFIG, LINE_CONFIG)
from other.questions.x_questions import x_questions_btn_func
from other.questions.y_questions import y_questions_btn_func
import re
import math
import webbrowser


def menu_func(root, exp_pic, line_pic, gh_image,
              w_gh_image, questions, w_questions):
    """
    Функция главного меню
    """
    pattern = r"^-?\d{1,8}(\.\d{1,8})?$"

    def calc_btn_func(event):
        """
        Функция кнопки "Вычислить"
        """
        # проверки на совпадение паттерну
        if not re.match(pattern, xent.get()) and not re.match(pattern, yent.get()):
            ans_lbl.config(text="Некорректный ввод x и y!",
                           **TEXT_CONFIG)
            ans_lbl.place(x=280, y=420)
            return
        elif not re.match(pattern, xent.get()):
            ans_lbl.config(text="Некорректный ввод x!",
                           **TEXT_CONFIG)
            ans_lbl.place(x=295, y=420)
            return
        elif not re.match(pattern, yent.get()):
            ans_lbl.config(text="Некорректный ввод y!",
                           **TEXT_CONFIG)
            ans_lbl.place(x=295, y=420)
            return

        try:
            x = float(xent.get())
            y = float(yent.get())
            ans = round(math.log((x * y) / (4 - math.pow(x, 2))) + math.asin(x / y), 6)

            ans_lbl.config(text=ans)
            ans_lbl.place(x=355, y=420)

        except ValueError:
            ans_lbl.config(text="Нет решения!",
                           **TEXT_CONFIG)
            ans_lbl.place(x=330, y=420)

        except ZeroDivisionError:
            ans_lbl.config(text="Деление на ноль!",
                           **TEXT_CONFIG)
            ans_lbl.place(x=315, y=420)

    def gh_btn_func():
        """
        Функция для открытия моего профиля ГитХаба))
        """
        webbrowser.open("https://github.com/mwh4t")

    # текст "вычислить значение выражения:"
    title = Label(text="Вычислить значение выражения:",
                  **TEXT_CONFIG)
    title.place(x=250, y=8)

    # картинка с выражением
    exp = Label(image=exp_pic, **EXP_CONFIG)
    exp.place(x=190, y=80)

    # текст "х ="
    xlbl = Label(text="x =", **TEXT_CONFIG)
    xlbl.place(x=280, y=227)
    # поле ввода для х
    xent = Entry()
    xent.place(x=320, y=230)
    # кнопка "вопросы по х"
    x_questions_btn = CircleButton(image=questions, **CIRCLE_BTN_CONFIG,
                                   activeimage=w_questions,
                                   command=lambda: x_questions_btn_func(root))
    x_questions_btn.config(width=28)
    x_questions_btn.place(x="512", y="228")

    # текст "у ="
    ylbl = Label(text="y =", **TEXT_CONFIG)
    ylbl.place(x=280, y=307)
    # поле ввода для у
    yent = Entry()
    yent.place(x=320, y=310)
    # кнопка "вопросы по y"
    y_questions_btn = CircleButton(image=questions, **CIRCLE_BTN_CONFIG,
                                   activeimage=w_questions,
                                   command=lambda: y_questions_btn_func(root))
    y_questions_btn.config(width=28)
    y_questions_btn.place(x="512", y="308")

    # текст с ответом
    ans_lbl = Label(text="", **TEXT_CONFIG)
    ans_lbl.place(x=300, y=420)

    # картинка с линией
    line_lbl = Label(image=line_pic, **LINE_CONFIG)
    line_lbl.place(x=270, y=445)

    # кнопка "вычислить"
    calc_btn = Button(text="Вычислить", **BTN_CONFIG,
                      command=lambda event=None: calc_btn_func(event))
    calc_btn.place(x=330, y=550)
    root.bind("<KeyPress-Return>", calc_btn_func)  # по нажатию Enter

    # кнопка-ссылка на ГитХаб
    gh_btn = CircleButton(image=gh_image, activeimage=w_gh_image,
                          **CIRCLE_BTN_CONFIG, command=lambda: gh_btn_func())
    gh_btn.place(x="8", y="555")
