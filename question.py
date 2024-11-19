import json

class Question:
    def __init__(self, question_text, answer, options=None):
        self.question_text = question_text
        self.answer = answer
        self.options = options or []

class QuestionBank:
    def __init__(self, filename):
        self.questions = self.load_questions(filename)
        self.current_question_index = 0

    def load_questions(self, filename):
        """Soruları JSON dosyasından yükler."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return [Question(q['question_text'], q['answer'], q['options']) for q in data]
        except FileNotFoundError:
            print(f"Error: {filename} not found.")
            return []

    def next_question(self):
        """Sonraki soruyu döndürür."""
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

    def has_more_questions(self):
        """Daha fazla soru olup olmadığını kontrol eder."""
        return self.current_question_index < len(self.questions)
