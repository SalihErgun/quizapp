'''import random
import json

class Question:
    def __init__(self, section):
        self.section = section
        self.questions = self.load_questions()

    def load_questions(self):
        # JSON dosyasını yükle
        with open(f'questions_section{self.section}.json', 'r') as f:
            return json.load(f)

    def ask_question(self):
        # Bölümden rastgele bir soru seç
        selected_question = random.choice(self.questions)
        print(f"Question: {selected_question['question_text']}")
        print(f"Type: {selected_question['type']}")
        print("Options:")
        for idx, option in enumerate(selected_question['options'], 1):
            print(f"{idx}. {option}")

        # Kullanıcıdan cevap al
        user_answer = input("Your answer(s): ").strip()

        # Doğru cevabı al
        correct_answer = self.get_correct_answer(selected_question)

        # True-False veya Single-Choice sorularda virgül olmadan tek cevap beklenir
        if selected_question['type'] in ['True-False', 'Single-Choice']:
            # `Single-Choice` veya `True-False` sorular için doğru cevap tek bir string olarak alınır
            if user_answer.lower() == correct_answer.lower():  # Küçük harfe çevirerek karşılaştır
                print("Correct!")
                return 1
            else:
                print(f"Wrong! The correct answer is: {correct_answer}")
                return 0
        else:
            # Multiple-Choice sorularda birden fazla cevap beklenebilir
            user_answer = user_answer.split(",")  # Virgülleri ayırarak liste yap
            user_answer_set = set([answer.strip().lower() for answer in user_answer])  # Küçük harfe çevir ve temizle
            correct_answer_set = set([ans.lower() for ans in correct_answer])  # Küçük harfe çevir

            if user_answer_set == correct_answer_set:
                print("Correct!")
                return 1
            else:
                print(f"Wrong! The correct answers are: {', '.join(correct_answer)}")
                return 0

    def get_correct_answer(self, question):
        # Cevapları answers.json dosyasından yükle
        with open('answers.json', 'r') as f:
            answers = json.load(f)
            return answers.get(str(question['id']), "")
'''

'''import random
import json

class Question:
    def __init__(self, section):
        self.section = section
        self.questions = self.load_questions()

    def load_questions(self):
        # JSON dosyasını yükle
        try:
            with open(f'questions_section{self.section}.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: 'questions_section{self.section}.json' not found!")
            return []

    def ask_question(self):
        # Bölümden rastgele bir soru seç
        if not self.questions:
            print("No questions available.")
            return 0
        
        selected_question = random.choice(self.questions)
        print(f"Question: {selected_question['question_text']}")
        print(f"Type: {selected_question['type']}")
        print("Options:")
        for idx, option in enumerate(selected_question['options'], 1):
            print(f"{idx}. {option}")

        # Kullanıcıdan cevap al
        user_answer = input("Your answer(s): ").strip()

        # Doğru cevabı al
        correct_answer = self.get_correct_answer(selected_question)

        # True-False veya Single-Choice sorularda virgül olmadan tek cevap beklenir
        if selected_question['type'] in ['True-False', 'Single-Choice']:
            # `Single-Choice` veya `True-False` sorular için doğru cevap tek bir string olarak alınır
            if user_answer.lower() == correct_answer.lower():  # Küçük harfe çevirerek karşılaştır
                print("Correct!")
                return 1
            else:
                print(f"Wrong! The correct answer is: {correct_answer}")
                return 0
        else:
            # Multiple-Choice sorularda birden fazla cevap beklenebilir
            user_answer = user_answer.split(",")  # Virgülleri ayırarak liste yap
            user_answer_set = set([answer.strip().lower() for answer in user_answer])  # Küçük harfe çevir ve temizle
            correct_answer_set = set([ans.lower() for ans in correct_answer])  # Küçük harfe çevir

            if user_answer_set == correct_answer_set:
                print("Correct!")
                return 1
            else:
                print(f"Wrong! The correct answers are: {', '.join(correct_answer)}")
                return 0

    def get_correct_answer(self, question):
        # Cevapları answers.json dosyasından yükle
        try:
            with open('answers.json', 'r') as f:
                answers = json.load(f)
                return answers.get(str(question['id']), "")
        except FileNotFoundError:
            print("Error: 'answers.json' file not found.")
            return ""'''

'''import random
import json

class Question:
    def __init__(self, section):
        self.section = section
        self.questions = self.load_questions()
        self.randomized_questions = self.randomize_questions()  # Soruları bir kere karıştırıyoruz
        self.current_question_index = 0  # Sunulacak ilk soru

    def load_questions(self):
        try:
            with open(f'questions_section{self.section}.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: 'questions_section{self.section}.json' not found!")
            return []

    def randomize_questions(self):
        """Soruları bir kez rastgele sıraya koyar."""
        randomized_questions = self.questions[:]
        random.shuffle(randomized_questions)
        return randomized_questions

    def ask_question(self):
        # Tüm sorular sorulduysa kullanıcıya bildirim yap
        if self.current_question_index >= len(self.randomized_questions):
            print("All questions in this section have been asked.")
            return 0

        # Sıradaki soruyu al
        selected_question = self.randomized_questions[self.current_question_index]
        self.current_question_index += 1  # Bir sonraki soru için sırayı ilerlet

        print(f"Question: {selected_question['question_text']}")
        print(f"Type: {selected_question['type']}")

        # Tüm seçenekler için numaralandırma
        options_mapping = {}
        if selected_question['type'] == 'True-False':
            options_mapping = {"1": "True", "2": "False"}
        else:
            options_mapping = {str(idx): option for idx, option in enumerate(selected_question['options'], 1)}

        for idx, option in options_mapping.items():
            print(f"{idx}. {option}")

        # Kullanıcı yanıtını alırken hem metin hem numara desteği
        user_answer = input("Your answer(s) (You can use numbers or text): ").strip()
        correct_answer = self.get_correct_answer(selected_question)

        if selected_question['type'] in ['True-False', 'Single-Choice']:
            return self.handle_single_choice_or_true_false(selected_question, user_answer, correct_answer, options_mapping)
        else:
            return self.handle_multiple_choice(selected_question, user_answer, correct_answer, options_mapping)

    def handle_single_choice_or_true_false(self, question, user_answer, correct_answer, options_mapping):
        user_answer_normalized = options_mapping.get(user_answer.strip(), user_answer).lower()
        correct_answer_normalized = correct_answer.lower()

        if user_answer_normalized == correct_answer_normalized:
            print("Correct!")
            return question.get('score', 0)  # Bu soruya atanmış puanı döndür
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")
            return 0

    def handle_multiple_choice(self, question, user_answer, correct_answer, options_mapping):
        user_answer_set = set(
            options_mapping.get(ans.strip(), ans.strip()).lower() 
            for ans in user_answer.split(',')
        )
        correct_answer_set = set(ans.lower() for ans in correct_answer)

        total_correct_answers = len(correct_answer_set)
        score_per_answer = question.get('score', 0) / total_correct_answers if total_correct_answers else 0

        user_score = 0
        for answer in user_answer_set:
            if answer in correct_answer_set:
                user_score += score_per_answer
        
        print(f"Your score for this question: {user_score}")
        return user_score

    def get_correct_answer(self, question):
        try:
            with open('answers.json', 'r') as f:
                answers = json.load(f)
                return answers.get(str(question['id']), "")
        except FileNotFoundError:
            print("Error: 'answers.json' file not found.")
            return ""
'''

'''import random
import json

class Question:
    def __init__(self, section):
        self.section = section
        self.questions = self.load_questions()
        self.randomized_questions = self.randomize_questions()  # Soruları bir kere karıştırıyoruz
        self.current_question_index = 0  # Sunulacak ilk soru

    def load_questions(self):
        try:
            with open(f'questions_section{self.section}.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: 'questions_section{self.section}.json' not found!")
            return []

    def randomize_questions(self):
        """Soruları bir kez rastgele sıraya koyar."""
        randomized_questions = self.questions[:]
        random.shuffle(randomized_questions)
        return randomized_questions

    def ask_question(self):
        # Tüm sorular sorulduysa kullanıcıya bildirim yap
        if self.current_question_index >= len(self.randomized_questions):
            print("All questions in this section have been asked.")
            return 0

        # Sıradaki soruyu al
        selected_question = self.randomized_questions[self.current_question_index]
        self.current_question_index += 1  # Bir sonraki soru için sırayı ilerlet

        print(f"Question: {selected_question['question_text']}")
        print(f"Type: {selected_question['type']}")

        # Tüm seçenekler için numaralandırma
        options_mapping = {}
        if selected_question['type'] == 'True-False':
            options_mapping = {"1": "True", "2": "False"}
        else:
            options_mapping = {str(idx): option for idx, option in enumerate(selected_question['options'], 1)}

        for idx, option in options_mapping.items():
            print(f"{idx}. {option}")

        # Kullanıcı yanıtını alırken hem metin hem numara desteği
        user_answer = input("Your answer(s) (You can use numbers or text): ").strip()
        correct_answer = self.get_correct_answer(selected_question)

        if selected_question['type'] in ['True-False', 'Single-Choice']:
            return self.handle_single_choice_or_true_false(selected_question, user_answer, correct_answer, options_mapping)
        else:
            return self.handle_multiple_choice(selected_question, user_answer, correct_answer, options_mapping)

    def handle_single_choice_or_true_false(self, question, user_answer, correct_answer, options_mapping):
        user_answer_normalized = options_mapping.get(user_answer.strip(), user_answer).lower()
        correct_answer_normalized = correct_answer.lower()

        if user_answer_normalized == correct_answer_normalized:
            print("Correct!")
            return question.get('score', 0)  # Bu soruya atanmış puanı döndür
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")
            return 0

    def handle_multiple_choice(self, question, user_answer, correct_answer, options_mapping):
        user_answer_set = set(
            options_mapping.get(ans.strip(), ans.strip()).lower() 
            for ans in user_answer.split(',')
        )
        correct_answer_set = set(ans.lower() for ans in correct_answer)

        total_correct_answers = len(correct_answer_set)
        score_per_answer = question.get('score', 0) / total_correct_answers if total_correct_answers else 0

        user_score = 0
        for answer in user_answer_set:
            if answer in correct_answer_set:
                user_score += score_per_answer
        
        print(f"Your score for this question: {user_score}")
        return user_score

    def get_correct_answer(self, question):
        try:
            with open('answers.json', 'r') as f:
                answers = json.load(f)
                return answers.get(str(question['id']), "")
        except FileNotFoundError:
            print("Error: 'answers.json' file not found.")
            return ""
'''

import random
import json

class Question:
    def __init__(self, section):
        self.section = section
        self.questions = self.load_questions()
        self.randomized_questions = self.randomize_questions()  # Soruları bir kere karıştırıyoruz
        self.current_question_index = 0  # Sunulacak ilk soru
        self.question_score = 20  # Her soru için verilecek puan

    def load_questions(self):
        try:
            with open(f'questions_section{self.section}.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: 'questions_section{self.section}.json' not found!")
            return []

    def randomize_questions(self):
        """Soruları bir kez rastgele sıraya koyar."""
        randomized_questions = self.questions[:]
        random.shuffle(randomized_questions)
        return randomized_questions

    def ask_question(self):
        # Tüm sorular sorulduysa kullanıcıya bildirim yap
        if self.current_question_index >= len(self.randomized_questions):
            print("All questions in this section have been asked.")
            return 0

        # Sıradaki soruyu al
        selected_question = self.randomized_questions[self.current_question_index]
        self.current_question_index += 1  # Bir sonraki soru için sırayı ilerlet

        print(f"Question: {selected_question['question_text']}")
        print(f"Type: {selected_question['type']}")

        # Tüm seçenekler için numaralandırma
        options_mapping = {}
        if selected_question['type'] == 'True-False':
            options_mapping = {"1": "True", "2": "False"}
        else:
            options_mapping = {str(idx): option for idx, option in enumerate(selected_question['options'], 1)}

        for idx, option in options_mapping.items():
            print(f"{idx}. {option}")

        # Kullanıcı yanıtını alırken hem metin hem numara desteği
        user_answer = input("Your answer(s) (You can use numbers or text): ").strip()
        correct_answer = self.get_correct_answer(selected_question)

        if selected_question['type'] in ['True-False', 'Single-Choice']:
            return self.handle_single_choice_or_true_false(selected_question, user_answer, correct_answer, options_mapping)
        else:
            return self.handle_multiple_choice(selected_question, user_answer, correct_answer, options_mapping)

    def handle_single_choice_or_true_false(self, question, user_answer, correct_answer, options_mapping):
        user_answer_normalized = options_mapping.get(user_answer.strip(), user_answer).lower()
        correct_answer_normalized = correct_answer.lower()

        if user_answer_normalized == correct_answer_normalized:
            print("Correct!")
            return self.question_score  # Her doğru cevap için standart puan
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")
            return 0

    def handle_multiple_choice(self, question, user_answer, correct_answer, options_mapping):
        user_answer_set = set(
            options_mapping.get(ans.strip(), ans.strip()).lower() 
            for ans in user_answer.split(',')
        )
        correct_answer_set = set(ans.lower() for ans in correct_answer)

        total_correct_answers = len(correct_answer_set)
        score_per_answer = self.question_score / total_correct_answers if total_correct_answers else 0

        user_score = 0
        for answer in user_answer_set:
            if answer in correct_answer_set:
                user_score += score_per_answer
        
        print(f"Your score for this question: {user_score}")
        return user_score

    def get_correct_answer(self, question):
        try:
            with open('answers.json', 'r') as f:
                answers = json.load(f)
                return answers.get(str(question['id']), "")
        except FileNotFoundError:
            print("Error: 'answers.json' file not found.")
            return ""
