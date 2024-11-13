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
        pass

    def display_question(self, question):
       pass


    def get_user_input(self, question):
        pass

    def validate_input(self, user_input, max_options):
        pass

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
        pass
