from tkinter import ttk, Scrollbar

from customtkinter import CTk, CTkCanvas, CTkFrame, CTkButton, CTkComboBox, CTkLabel

from functions import check_answers, easy_question


def get_info(root, num_questions, difficulty, number_of_questions_cb):
    root.destroy()
    root1 = CTk()
    root1.title("Test")
    h = root1.winfo_screenheight() // 2
    w = root1.winfo_screenwidth() // 2
    root1.geometry(f"350x350+{w}+{h}")
    canvas = CTkCanvas(root1, borderwidth=0)
    frame = CTkFrame(canvas)

    vsb = Scrollbar(root1, orient="horizontal", command=canvas.xview)
    vsb.grid(row=10, column=0, sticky="nsew")
    canvas.configure(xscrollcommand=vsb.set)
    canvas.grid(row=0, column=0, sticky="nsew")
    canvas.create_window((3, 2), window=frame, anchor="nw", tags="frame")
    my_notebook = ttk.Notebook(frame, width=600, height=600)
    my_notebook.grid(pady=15)

    def frame_configure(event, canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame.bind("<Configure>", lambda event: frame_configure(event, canvas))
    answers = []
    for i in range(int(num_questions)):
        question_frame = CTkFrame(my_notebook, width=200, height=200)
        question_frame.pack(fill="both", expand=1)
        my_notebook.add(question_frame, text=f"Question {i + 1}")

        if i == 0:
            question = "x: 7 + 25 = 34"
            options = ["63", "56", "62", "57", "58"]
        elif i == 1:
            question = "6 * 3 + x = 72"
            options = ["x = 8", "x = 9", "x = 6", "x = 5"]
        elif i == 2:
            question = "401 949 338 + 499 427 394 ="
            options = ["901376732", "90136731", "5024983", "5024982"]
        elif i == 3:
            question = "Перетворіть в метри: 12 дм, 54 см"
            options = ["1 м 2 дм, 0,54 м", "1 м 3 дм, 0,054 м", "0,12 м, 0,0054 дм"]
        elif i == 4:
            question = "Виконайте дію: 5,37 * 39 ="
            options = ["102,23", "425,52", "208,43", "209,43"]
        elif i == 5:
            question = "Спростіть вираз 2,1с-0,6с+3,9с"
            options = ["5,4с", "6,6с", "5,8с", "5,2с"]
        elif i == 6:
            question = "Скільки знаків після коми має бути в добутку 12,3 · 7,356 ?"
            options = ["один", "два", "три", "чотири"]
        elif i == 7:
            question = "Обчисліть 6,25 · 3,4 ="
            options = ["212,5", "21,25", "2125", "2,125"]
        elif i == 8:
            question = "Обчисліть зручним способом:  50 · 1,25 · 0,1 · 8 ="
            options = ["5", "(50⋅1,25)⋅(0,1⋅8)", "(50⋅0,1)⋅(1,25⋅8)", "50"]
        elif i == 9:
            question = "Обчисліть добуток: 2,75×0,1="
            options = ["27,5", "2,75", "0,275", "275"]
        elif i == 10:
            question = "Обчисліть добуток: 5,8×1000="
            options = ["5800", "580", "0,58", "58000"]
        elif i == 11:
            question = "Обчисли зручним способом: 7,19 ⋅ 41,36 + 7,19 ⋅ 58,64"
            options = ["7,19(41,36+58,64)", "71,9", "719", "297,3784+421,6216"]
        elif i == 12:
            question = "Виконайте множення: 0,526 ⋅ 7,095"
            options = ["373,197", "37,3197", "3,73197", "3,83197"]
        elif i == 13:
            question = "На яке число треба помножити число 8,03, щоб отримати число 8030"
            options = ["1000", "10", "0,01", "100"]
        elif i == 14:
            question = "Обчислити 8,956*10"
            options = ["895,6", "89,56", "89560", "895600"]
        elif i == 15:
            question = "3,2104 ⋅ 100"
            options = ["32104", "3210,4", "321,04", "3,2104"]
        elif i == 16:
            question = "568,6*1000"
            options = ["56,86", "568600", "56860", "5,686"]
        elif i == 17:
            question = "Обчислити 2,2•1,99"
            options = ["4,21", "Не знаю", "4,378"]
        elif i == 18:
            question = "Обчислити 23,15*0,1="
            options = ["231,5", "2315", "2,315", "23150"]
        elif i == 18:
            question = "Обчислити 852,235*0,001"
            options = ["0,852235", "8522,35", "85223,5", "852235"]
        elif i == 19:
            question = "Виразити в метрах 5 см"
            options = ["0,05 м", "0,005 м", "0,5 м", "0,50 м"]
        elif i == 20:
            question = "Виразіть 1562 м у кілометрах."
            options = ["0,1562 км", "15,62 км", "1,562 км", "156,2 км"]
        elif i == 21:
            question = "Виразіть 1562 м у кілометрах."
            options = ["0,1562 км", "15,62 км", "1,562 км", "156,2 км"]
        elif i == 22:
            question = "Виразіть 1562 м у кілометрах."
            options = ["0,1562 км", "15,62 км", "1,562 км", "156,2 км"]
        elif i == 23:
            question = "Виразіть 1562 м у кілометрах."
            options = ["0,1562 км", "15,62 км", "1,562 км", "156,2 км"]

        selected_answer = easy_question(question_frame, question, options)
        answers.append(selected_answer)

    finish_btn = CTkButton(root1, text="Finish test", width=150, height=30, border_color="grey", fg_color="white",
                           text_color="grey",
                           border_width=1, hover_color="#A9A9A9",
                           command=lambda: check_answers(answers, root1, difficulty, number_of_questions_cb))
    finish_btn.grid(row=1, column=0, pady=(20, 0))

    root1.mainloop()


def main():
    root = CTk()
    root.title("Test")
    x_coordinate = root.winfo_screenwidth() // 2
    y_coordinate = root.winfo_screenheight() // 2

    root.geometry(f"300x300+{x_coordinate}+{y_coordinate}")

    number_of_questions_lab = CTkLabel(root, text="Number of questions", width=30, height=30)
    number_of_questions_lab.grid(row=0, column=1, pady=(20, 0), padx=100)
    number_of_questions_cb = CTkComboBox(root, values=["1", "6", "8", "10", "12", "24"], state="readonly", width=120)
    number_of_questions_cb.set("6")
    number_of_questions_cb.grid(row=1, column=1, pady=0)

    difficulty_lab = CTkLabel(root, text="Difficulty", width=30, height=30)
    difficulty_lab.grid(row=2, column=1, pady=(20, 0))
    difficulty_cb = CTkComboBox(root, values=["Easy", "Medium", "Hard"], state="readonly", width=120)
    difficulty_cb.set("Easy")
    difficulty_cb.grid(row=3, column=1, padx=20)

    submit_btn = CTkButton(root, text="Start test", width=150, height=30, border_color="grey", fg_color="white",
                           text_color="grey",
                           border_width=1, hover_color="#A9A9A9",
                           command=lambda: get_info(root, number_of_questions_cb.get(), difficulty_cb.get(),
                                                    number_of_questions_cb.get()))
    submit_btn.grid(row=4, column=1, pady=(20, 0), padx=20)
    root.mainloop()


if __name__ == "__main__":
    main()
