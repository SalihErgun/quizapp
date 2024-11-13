import time
#from Question import Question
#from Timer import Timer
#from Result import Result

class Exam:
    def __init__(self, user, questions):
        """
        Exam sınıfı, kullanıcının sınavını yönetir.
        :param user: Kullanıcı nesnesi (User class)
        :param questions: Sorular listesi (Question class nesneleri)
    
        The Exam class manages the user's exam.
        :param user: User object (User class)
        :param questions: List of questions (Question class objects)
         """
        self.user = user
        self.questions = questions
        #self.timer = Timer(time_limit=1800)  # 30 dakika sınav süresi
        self.user_answers = []
        #self.result = Result()
        self.exam_active = False
        

    def start_exam(self):
        """
        Sınavı başlatır ve kullanıcıya soruları sırayla sorar.
        """
        print(f"\nHoş geldiniz {self.user.name} {self.user.surname}! Sınavınız başlıyor.")
        self.exam_active = True
        self.timer.start_timer()

        for index, question in enumerate(self.questions):
            if self.time_out():
                print("\nSüre doldu! Sınav sona erdi.")
                break
            self.display_question(question)
            user_input = self.get_user_input(question)
            self.user_answers.append((question, user_input))

        self.end_exam()
        

    def display_question(self, question):
       
        """
        Kullanıcıya soruyu ve seçenekleri gösterir.
        """
        print(f"\nSoru: {question.question_text}")
        for idx, option in enumerate(question.options, start=1):
            print(f"{idx}. {option}")

        
       


    def get_user_input(self, question):
        while True:
            try:
                answer = int(input("Cevabınızı girin (seçenek numarası): "))
                if self.validate_input(answer, len(question.options)):
                    return answer
                else:
                    print("Geçersiz giriş. Lütfen seçenek numarasını girin.")
            except ValueError:
                print("Lütfen geçerli bir numara girin.")
        

    def validate_input(self, user_input, max_options):

        """
        Kullanıcı girdisinin geçerli bir seçenek olup olmadığını kontrol eder.
        """
        return 1 <= user_input <= max_options
        

    def time_out(self):
        """
        Sınav süresinin dolup dolmadığını kontrol eder.
        """
        return not self.timer.check_time()

    def end_exam(self):
        """
        Sınavı sonlandırır ve sonuçları hesaplar.
        """
        #print("\nSınav tamamlandı. Sonuçlar hesaplanıyor...")
        #self.calculate_results()
        #self.show_results()
        #self.user.update_attempts()
    
    

    def calculate_results(self):
        pass

    def show_results(self):
        """
         Kullanıcıya sınav sonucunu gösterir.
        """
        print(f"\n{self.user.name} {self.user.surname} için sınav sonucu:")
        print(f"Toplam Skor: {self.result.overall_score:.2f}%")
        if self.result.overall_score >= 50:
            print("Başarılı!")
        else:
            print("Başarısız.")

        
