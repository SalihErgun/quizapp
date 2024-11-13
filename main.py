'''from user import User
from question import Question

def start_exam():
    # Getting user input for username, surname, and student number
    username = input("Enter your username: ")
    surname = input("Enter your surname: ")
    student_number = input("Enter your student number: ")

    # Create a User instance
    user = User(username, surname, student_number)

    # Load user data (for example, check if the user exists in the database)
    user.load_user_data()  # This method handles both loading and saving the user data.

    # Check if the user has attempts left
    if not user.has_attempts_left():
        print(f"{username}, you have exceeded the number of allowed attempts.")
        return

    # Start the exam and increment the attempt count
    user.increment_attempts()
    user.save_user_data()  # Save the updated user data after incrementing attempts
    print(f"Welcome {username} {surname}!")

    # Iterate through each section of the exam
    total_score = 0
    for section in range(1, 5):  # 4 sections in total
        print(f"\nStarting Section {section}...")

        # Instantiate the Question class for this section
        question = Question(section)

        correct_answers = 0
        total_questions = 5  # Number of questions per section

        # Ask each question in the section
        for _ in range(total_questions):
            score = question.ask_question()  # This will return 1 for correct answer, 0 for wrong
            correct_answers += score

        # Update the section score
        user.update_score(f"section{section}", correct_answers, total_questions)
        total_score += correct_answers  # Accumulate total correct answers across all sections

    # Save the final user data after the exam
    user.save_user_data()

    # Display the overall score
    overall_score = (total_score / (5 * 4)) * 100  # Total correct answers divided by total possible answers
    print(f"Your overall success score is {overall_score:.2f}%")

    # Check if the user passed or failed
    if overall_score >= 75:  # For example, passing score is 75%
        print("You passed the exam!")
    else:
        print("You failed the exam.")

if __name__ == "__main__":
    start_exam()'''


'''
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
    for section in range(1, 5):
        print(f"\nStarting Section {section}...")

        question = Question(section)  # Soru setini oluştur
        correct_answers = 0
        total_questions = 5  # Her bölümde 5 soru olduğunu varsayıyoruz

        for _ in range(total_questions):
            score = question.ask_question()  # Soruyu sor
            correct_answers += score  # Doğru cevap sayısını ekle

        user.update_score(f"section{section}", correct_answers, total_questions)
        total_score += correct_answers  # Toplam puana ekle

    user.save_user_data()

    # Başarı oranını hesapla
    overall_score = (total_score / (5 * 4)) * 100  # 5 soru ve 4 bölüm var
    print(f"Your overall success score is {overall_score:.2f}%")

    if overall_score >= 75:
        print("You passed the exam!")
    else:
        print("You failed the exam.")

if __name__ == "__main__":
    start_exam()
'''
'''from user import User
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
    print(f"Welcome {username} {surname}!\n")

    total_score = 0  # Toplam puan
    for section in range(1, 5):
        print(f"\nStarting Section {section}...")

        question = Question(section)  # Soru setini oluştur
        correct_answers = 0
        total_questions = 5  # Her bölümde 5 soru olduğunu varsayıyoruz

        for _ in range(total_questions):
            score = question.ask_question()  # Soruyu sor
            correct_answers += score  # Doğru cevap sayısını ekle

        # Bölüm puanını hesapla
        user.update_score(f"section{section}", correct_answers, total_questions)
        section_score = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
        total_score += correct_answers  # Toplam puana ekle

        print(f"\nSection {section} completed.")
        print(f"Correct Answers in Section {section}: {correct_answers}/{total_questions}")
        print(f"Section {section} Score: {section_score:.2f}%")
        print(f"Total Score So Far: {total_score} points\n")

    user.save_user_data()

    # Başarı oranını hesapla
    overall_score = (total_score / (5 * 4)) * 100  # 5 soru ve 4 bölüm var
    print(f"Your overall success score is {overall_score:.2f}%")

    if overall_score >= 75:
        print("You passed the exam!")
    else:
        print("You failed the exam.")

if __name__ == "__main__":
    start_exam()
'''

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
        section_score = user.success_per_section[f"section{section}"]
        total_score += section_score  # Toplam puana ekle

        print(f"Section {section} completed. Correct Answers: {correct_answers}/{total_questions}, Score: {section_score:.2f}/100")

    user.save_user_data()

    # Başarı oranını hesapla
    overall_score = user.get_score()
    print(f"Your overall success score is {overall_score:.2f}%")

    if overall_score >= 75:
        print("You passed the exam!")
    else:
        print("You failed the exam.")

if __name__ == "__main__":
    start_exam()
