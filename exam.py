class Exam:
    def __init__(self, question_bank, answers):
        self.question_bank = question_bank  # Sınav soruları
        self.answers = answers  # Doğru cevaplar
        self.score = 0  # Başlangıçta puan 0

    def check_answer(self, question_id, user_answer):
        """Kullanıcının cevabını kontrol eder ve doğru/yanlış kontrolü yapar."""
        correct_answer = self.answers.get(str(question_id))  # Sorunun doğru cevabı
        if correct_answer is None:
            return False  # Sorunun ID'si geçerli değilse yanlış kabul et

        if isinstance(correct_answer, list):
            # Çoktan seçmeli (birden fazla doğru cevap)
            if isinstance(user_answer, list):
                # Doğru şık sayısına göre kontrol et
                if len(user_answer) == len(correct_answer) and sorted(user_answer) == sorted(correct_answer):
                    return True
        else:
            # Tek doğru cevap
            if user_answer == correct_answer:
                return True
        return False

    def calculate_score(self, responses):
        """Kullanıcı cevaplarına göre toplam puanı hesaplar."""
        self.score = 0  # Puanı sıfırlıyoruz
        for question_id, user_answer in responses.items():
            # Sorunun ID'sinin geçerli olup olmadığını kontrol et
            question = next((q for q in self.question_bank if q['id'] == question_id), None)
            if question is not None and self.check_answer(question_id, user_answer):
                self.score += question.get('score', 0)  # Sorunun puanını ekle
        return self.score
