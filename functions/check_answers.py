from customtkinter import CTk, CTkLabel, CTkButton

from functions import save_results, new


def check_answers(answers, root1, difficulty, number_of_questions_cb):
    correct_answers = 0
    expected_answers = [
        "63", "209,43", "x = 6", "1 м 2 дм, 0,54 м", "901376732",
        "5,4с", "один", "212,5", "5", "0,275", "5800",
        "7,19(41,36+58,64)", "373,197", "100", "89560", "32104",
        "568600", "4,21", "2,315", "0,852235", "0,05 м", "1,562 км"
    ]
    for answer in answers:
        if answer.get() in expected_answers:
            correct_answers += 1

    print(f"Total correct answers: {correct_answers}")
    root1.destroy()

    result_root = CTk()
    result_root.title("Result")
    w = 300
    h = 300
    x_coordinate = (result_root.winfo_screenwidth() - w) // 2
    y_coordinate = (result_root.winfo_screenheight() - h) // 2
    result_root.geometry(f"{w}x{h}+{x_coordinate}+{y_coordinate}")

    rez = CTkLabel(result_root, text=f"Correct answers: {correct_answers}/{number_of_questions_cb}")
    rez.pack(pady=20)
    rate = CTkLabel(result_root,
                    text=f"Correct answer rate: {round(int(correct_answers) / int(number_of_questions_cb) * 100)}%")
    rate.pack(pady=(0, 20))
    rez1 = CTkLabel(result_root, text=f"Difficulty: {difficulty}")
    rez1.pack(pady=(0, 20))
    save = CTkButton(result_root, text="Save results", border_color="grey", fg_color="white",
                     text_color="grey", border_width=1, hover_color="#A9A9A9",
                     command=lambda: save_results(correct_answers, number_of_questions_cb, difficulty))
    save.pack(pady=(0, 20))
    rez2 = CTkButton(result_root, text="Create New Test", command=lambda: new(result_root), border_color="grey",
                     fg_color="white", text_color="grey", border_width=1, hover_color="#A9A9A9")
    rez2.pack(pady=10)

    result_root.mainloop()
