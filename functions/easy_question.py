from customtkinter import StringVar, CTkLabel, CTkRadioButton


def easy_question(frame, question, options):
    selected_answer = StringVar()

    question_lb = CTkLabel(frame, text=question)
    question_lb.grid(row=0, column=0, pady=20)

    for q, option in enumerate(options):
        rad = CTkRadioButton(frame, text=option, variable=selected_answer, value=option)
        rad.grid(row=q + 1, column=0, sticky='w')

    return selected_answer
