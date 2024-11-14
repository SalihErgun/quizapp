from user import User
from question import Question

def start_exam():
    username = input("Enter your username: ")
    surname = input("Enter your surname: ")
    student_number = input("Enter your student number: ")

    user = User(username, surname, student_number)

    # Kullanıcı verilerini yükle
    user.load_user_data()

    if not user.has_attempts_left():
        print(f"{username}, you have exceeded the number of allowed attempts.")
        return

    user.increment_attempts()
    user.save_user_data()
    print(f"Welcome {username} {surname}!")

    total_score = 0  # Toplam puan
    all_sections_passed = True  # Her bölümün başarıyla geçildiğini kontrol etmek için

    for section in range(1, 5):
        print(f"\nStarting Section {section}...")

        question = Question(section)  # Soru setini oluştur
        correct_answers = 0
        total_questions = 5  # Her bölümde 5 soru olduğunu varsayıyoruz

        for _ in range(total_questions):
            score = question.ask_question()  # Soruyu sor
            correct_answers += (score / question.question_score)  # Doğru cevap sayısını ekle

        # Her bölüm sonunda başarıyı kullanıcıya göster
        user.update_score(f"section{section}", correct_answers, total_questions)
        section_score = round(user.success_per_section[f"section{section}"], 2)  # Bölüm puanını yuvarla
        total_score += section_score  # Toplam puana ekle

        # Bölüm puanı 100 üzerinden ve virgül sonrası 2 basamağa sınırlanmış şekilde gösteriliyor
        print(f"Section {section} completed. Correct Answers: {round(correct_answers, 2)}/{total_questions}, Score: {section_score:.2f}/100")

        # Bölümde %50 başarıdan azsa, öğrenciyi başarısız say
        if section_score < 50:
            all_sections_passed = False

    user.save_user_data()

    # Genel başarıyı hesapla
    overall_score = round(user.get_score(), 2)  # Genel başarıyı yuvarla

    # Genel başarıyı virgül sonrası 2 basamağa yuvarla
    print(f"Your overall success score is {overall_score:.2f}%")

    if overall_score >= 75 and all_sections_passed:
        print("You passed the exam!")
    else:
        print("You failed the exam.")

# Programın başlangıç noktası
if __name__ == "__main__":
    start_exam()

