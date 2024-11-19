import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root, exam):
        self.root = root
        self.exam = exam
        self.current_question_index = 0
        self.user_responses = {}
        self.time_left = 20 * 60  # Başlangıçta 20 dakika (1200 saniye)

        # Pencere başlığı ve boyutu
        self.root.title("Quiz Application")
        self.root.geometry("600x600")  # Pencere boyutunu sabitle

        # Arka plan rengi
        self.root.config(bg="#f2f2f2")

        # Zamanlayıcı etiketini başlatmadan önce kontrol et
        self.timer_label = None

        self.create_intro_screen()

    def format_time(self, seconds):
        """Zamanı dakika ve saniye formatında gösterir."""
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

    def start_exam(self):
        """Sınavı başlatır."""
        self.username = self.name_entry.get()
        self.surname = self.surname_entry.get()
        self.student_number = self.student_number_entry.get()
        if not all([self.username, self.surname, self.student_number]):
            messagebox.showerror("Error", "All fields must be filled!")
            return

        # Hoşgeldiniz ekranını temizle
        self.clear_window(exclude_timer=True)  # Zamanlayıcıyı silmeden temizle

        # Zamanlayıcıyı başlat
        self.update_timer()
        self.create_question_screen()

    def update_timer(self):
        """Zamanlayıcıyı günceller."""
        if self.timer_label is None:
            # Eğer timer_label eksikse, ekle
            self.timer_label = tk.Label(self.root, text=f"Time Left: {self.format_time(self.time_left)}", font=("Arial", 14), bg="#f2f2f2")
            self.timer_label.pack(pady=10)

        if self.time_left > 0:
            self.time_left -= 1
            time_text = self.format_time(self.time_left)
            self.timer_label.config(text=f"Time Left: {time_text}")
            self.root.after(1000, self.update_timer)  # 1 saniye sonra kendini tekrar çağırır
        else:
            # Süre bittiğinde sınavı bitir
            self.show_results()

    def create_intro_screen(self):
        """Kullanıcı giriş ekranını oluşturur."""
        self.clear_window(exclude_timer=True)

        # Başlık etiketini stilize etme
        title_label = tk.Label(self.root, text="Welcome to the Quiz!", font=("Arial", 24), bg="#f2f2f2")
        title_label.pack(pady=20)

        # Giriş formu
        form_frame = tk.Frame(self.root, bg="#f2f2f2")
        form_frame.pack(pady=20)

        tk.Label(form_frame, text="Name:", font=("Arial", 12), bg="#f2f2f2").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Surname:", font=("Arial", 12), bg="#f2f2f2").grid(row=1, column=0, padx=10, pady=5)
        self.surname_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.surname_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Student Number:", font=("Arial", 12), bg="#f2f2f2").grid(row=2, column=0, padx=10, pady=5)
        self.student_number_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.student_number_entry.grid(row=2, column=1, padx=10, pady=5)

        start_button = tk.Button(self.root, text="Start Exam", font=("Arial", 14), command=self.start_exam, bg="#4CAF50", fg="white", padx=20, pady=10)
        start_button.pack(pady=30)

    def create_question_screen(self):
        """Soruları gösterir."""
        self.clear_window(exclude_timer=True)  # Zamanlayıcıyı silmeden temizle

        questions = self.exam.question_bank
        if self.current_question_index < len(questions):
            question = questions[self.current_question_index]

            # Başlık etiketini stilize etme
            tk.Label(self.root, text=question["question_text"], font=("Arial", 16, "bold"), bg="#f2f2f2", wraplength=550).pack(pady=20)

            # Çoktan seçmeli soru ise, şıkları ekleyelim
            if isinstance(self.exam.answers.get(str(question['id'])), list):
                # Şık sayısına göre, hangi şıkların işaretlenmesi gerektiğini belirleyelim
                num_choices = len(self.exam.answers[str(question['id'])])
                info_label = tk.Label(self.root, text=f"Please select exactly {num_choices} options.", font=("Arial", 12), bg="#f2f2f2", wraplength=550)
                info_label.pack(pady=10)

                self.selected_answers = []  # Seçilen cevapları tutmak için bir liste
                for option in question["options"]:
                    var = tk.BooleanVar()  # Checkbox'ın işaretlenip işaretlenmediğini kontrol etmek için
                    checkbox = tk.Checkbutton(self.root, text=option, variable=var, font=("Arial", 12), bg="#f2f2f2")
                    checkbox.pack(anchor="w", padx=20, pady=5)
                    self.selected_answers.append((option, var))  # Seçenek ve değişkeni sakla
            else:
                # Tek doğru cevabı olan soru için radio button kullan
                self.selected_answer = tk.StringVar(value="")
                for option in question["options"]:
                    tk.Radiobutton(self.root, text=option, variable=self.selected_answer, value=option, font=("Arial", 12), bg="#f2f2f2").pack(anchor="w", padx=20, pady=5)

            # İleri gitmek için butonlar
            navigation_frame = tk.Frame(self.root, bg="#f2f2f2")
            navigation_frame.pack(pady=20)

            if self.current_question_index > 0:
                back_button = tk.Button(navigation_frame, text="Back", font=("Arial", 14), command=self.previous_question, bg="#FFC107", fg="black", padx=20, pady=10)
                back_button.pack(side="left", padx=10)

            next_button = tk.Button(navigation_frame, text="Next", font=("Arial", 14), command=self.next_question, bg="#4CAF50", fg="white", padx=20, pady=10)
            next_button.pack(side="left", padx=10)

        else:
            self.show_results()

    def previous_question(self):
        """Önceki soruya dönmek için kullanılacak fonksiyon."""
        self.current_question_index -= 1
        self.create_question_screen()

    def next_question(self):
        """Sonraki soruya geçer."""
        question_id = self.exam.question_bank[self.current_question_index]['id']

        # Çoktan seçmeli sorularda, doğru sayıda şık seçildi mi kontrol et
        question = next(q for q in self.exam.question_bank if q['id'] == question_id)
        correct_answers = self.exam.answers.get(str(question_id))

        # Çoktan seçmeli soruysa
        if isinstance(correct_answers, list):
            selected_answers = [option for option, var in self.selected_answers if var.get()]
            if len(selected_answers) != len(correct_answers):
                messagebox.showerror("Error", f"Please select exactly {len(correct_answers)} options!")
                return
            self.user_responses[question_id] = selected_answers  # Seçilen doğru şıkları kaydet
        else:
            # Tek doğru cevaplı soru için
            user_answer = self.selected_answer.get()
            if not user_answer:
                messagebox.showerror("Error", "Please select an answer!")
                return
            self.user_responses[question_id] = user_answer  # Seçilen cevabı kaydet

        self.current_question_index += 1
        self.create_question_screen()

    def show_results(self):
        """Sonuçları gösterir."""
        self.clear_window(exclude_timer=True)  # Zamanlayıcıyı silmeden temizle
        score = self.exam.calculate_score(self.user_responses)
        tk.Label(self.root, text=f"Your score: {score}", font=("Arial", 18, "bold"), bg="#f2f2f2").pack(pady=20)
        exit_button = tk.Button(self.root, text="Exit", font=("Arial", 14), command=self.root.quit, bg="#FF5733", fg="white", padx=20, pady=10)
        exit_button.pack(pady=30)

    def clear_window(self, exclude_timer=False):
        """Pencereyi temizler, opsiyonel olarak zamanlayıcıyı korur."""
        for widget in self.root.winfo_children():
            if not (exclude_timer and isinstance(widget, tk.Label) and widget == self.timer_label):
                widget.destroy()

