import json
import os

class QuestionBank:
    def __init__(self, question_files):
        self.questions = []
        for file in question_files:
            self.load_questions(file)

    def load_questions(self, file_path):
        """Belirtilen JSON dosyasından soruları yükler."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        with open(file_path, 'r') as file:
            data = json.load(file)
            self.questions.extend(data)

    def get_questions(self):
        """Tüm soruları döndürür."""
        return self.questions
