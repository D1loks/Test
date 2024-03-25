from tkinter import filedialog, messagebox


def save_results(correct_answers, number_of_questions_cb, difficulty):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.write(
                    f"Correct answers: {correct_answers}/{number_of_questions_cb}\n"
                    f"Correct answer rate: {round(int(correct_answers) / int(number_of_questions_cb) * 100)}%\n"
                    f"Difficulty: {difficulty}\n"
                )
            messagebox.showinfo("Succes", f"Результати збережено успішно в {file_path}")
        except Exception as e:
            messagebox.showerror("Error", "Сталася помилка під час збереження результатів: {e}")
    else:
        messagebox.showerror("Error", "Скасовано збереження результатів")
