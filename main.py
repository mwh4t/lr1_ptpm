from tkinter import *
from other.menu import menu_func


# создание основного окна
root = Tk()
root.title("Линейный алгоритм")
root.geometry("800x600")
root.geometry("+300+100")
root.resizable(False, False)

# цвет фона
root.configure(bg="#262626")

# изображение выражением
exp_pic = PhotoImage(file="other/pics/expression.png")

# изображение с линией
line_pic = PhotoImage(file="other/pics/line.png")

# изображения с ГитХабом
gh_image = PhotoImage(file="other/pics/gh.png")
w_gh_image = PhotoImage(file="other/pics/w_gh.png")

# изображения с вопросами
questions = PhotoImage(file="other/pics/questions.png")
w_questions = PhotoImage(file="other/pics/w_questions.png")

# функция главного меню
menu_func(root, exp_pic, line_pic, gh_image,
          w_gh_image, questions, w_questions)

# запуск основного цикла
root.mainloop()
