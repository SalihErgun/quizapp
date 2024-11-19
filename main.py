from gui import QuizApp
from question_bank import QuestionBank
from exam import Exam
from common import load_json
import tkinter as tk

if __name__ == "__main__":
    # Soru dosyaları ve cevap anahtarını yükle
    question_files = ["questions_section1.json", "questions_section2.json", "questions_section3.json", "questions_section4.json"]
    answers = load_json("answers.json")

    question_bank = QuestionBank(question_files)
    exam = Exam(question_bank.get_questions(), answers)

    # GUI'yi başlat
    root = tk.Tk()

    try:
        app = QuizApp(root, exam)

        # Pencere kapanırken yapılacak işlemleri tanımla
        root.protocol("WM_DELETE_WINDOW", root.quit)

        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")
        root.quit()
