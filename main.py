import os
import json
from user import User
from result import Result
from timer import Timer
from exam import Exam
from questions import Question


def main():
    # Dosya yolları
    user_data_path = "./data/users.json"
    questions_path = "./data/"
    answers_path = "./data/answers.json"
    time_limit = 300  # Sınav süresi (saniye cinsinden)

    # JSON dosyaları yoksa oluştur
    if not os.path.exists(user_data_path):
        with open(user_data_path, "w") as file:
            json.dump({}, file)

    # Kullanıcı girişini al
    print("Welcome to the Multi-Part Quiz Application!")
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    student_no = input("Enter your student number: ")

    users = User.load_user_data(user_data_path)
    if users is not None:
        print("User data loaded successfully")
    # Kullanıcıyı oluştur
    user = User(name, surname, student_no)

    # Kullanıcı doğrulaması
    with open(user_data_path, "r") as file:
        users = json.load(file)
        if student_no in users and users[student_no]["attempts"] >= 2:
            print("You have already used your 2 exam attempts. You cannot retake the exam.")
            return

    # Yeni bir kullanıcı ise veriyi kaydet
    if student_no not in users:
        user.save_user_data(user_data_path)

    # Zamanlayıcı ve sonuç nesnelerini oluştur
    timer = Timer(time_limit)
    result = Result()

    # Sınav nesnesini başlat
    exam = Exam(user, timer, result)

    # Sınavı başlat
    exam.start_exam()

    # Soruları yükle
    sections = [f"questions_section{i}.json" for i in range(1, 5)]
    question_bank = QuestionBank()

    for idx, section_file in enumerate(sections, 1):
        section_path = os.path.join(questions_path, section_file)
        with open(section_path, "r") as file:
            questions_data = json.load(file)
            for question in questions_data:
                q = Question(question["question"], question["options"], question["correct"])
                question_bank.add_question(f"Section {idx}", q)

    # Her bir bölüm için soruları seç ve kullanıcıdan cevap al
    for section in range(1, 5):
        print(f"--- Section {section} ---")
        random_questions = question_bank.get_random_questions(f"Section {section}", 5)

        section_results = []
        for question in random_questions:
            exam.display_question(question)
            user_answer = exam.get_user_input(question)
            while not exam.validate_input(user_answer, "multiple" if isinstance(question.correct_answer, list) else "single"):
                print("Invalid input! Please try again.")
                user_answer = exam.get_user_input(question)

            # Cevabı değerlendir
            is_correct = question.check_answer(user_answer)
            section_results.append(is_correct)

        # Sonuçları kaydet
        correct_answers = sum(section_results)
        result.section_scores[f"Section {section}"] = (correct_answers / len(random_questions)) * 100

    # Sınavı bitir ve sonuçları göster
    exam.end_exam()

if __name__ == "__main__":
    main()