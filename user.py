import json

class User:
    def __init__(self, username, surname, student_number):
        self.username = username
        self.surname = surname
        self.student_number = student_number
        self.attempts = 0
        self.score = 0
        self.max_attempts = 2
        self.success_per_section = {"section1": 0, "section2": 0, "section3": 0, "section4": 0}

    def load_user_data(self):
        try:
            with open("users.json", "r") as f:
                users_data = json.load(f)

            if self.username in users_data:
                user_data = users_data[self.username]
                self.attempts = user_data['attempts']
                self.score = user_data['score']
                self.success_per_section = user_data['success_per_section']
                self.student_number = user_data['student_number']
            else:
                print(f"User '{self.username}' not found in the database. Adding user...")
                self.save_user_data(users_data)
                
        except FileNotFoundError:
            print("users.json file not found. Creating a new one.")
            self.save_user_data()
        except json.JSONDecodeError:
            print("The users.json file is empty or corrupted. Creating a new one.")
            self.save_user_data()

    def save_user_data(self, users_data=None):
        if users_data is None:
            try:
                with open("users.json", "r") as f:
                    users_data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                users_data = {}

        if self.username not in users_data:
            users_data[self.username] = {
                "username": self.username,
                "surname": self.surname,
                "student_number": self.student_number,
                "attempts": self.attempts,
                "score": round(self.score, 2),  # Yuvarlama işlemi burada
                "success_per_section": {k: round(v, 2) for k, v in self.success_per_section.items()}  # Bölüm başarılarını yuvarla
            }
        else:
            users_data[self.username]["student_number"] = self.student_number
            users_data[self.username]["attempts"] = self.attempts
            users_data[self.username]["score"] = round(self.score, 2)  # Yuvarlama işlemi burada
            users_data[self.username]["success_per_section"] = {k: round(v, 2) for k, v in self.success_per_section.items()}  # Bölüm başarılarını yuvarla

        with open("users.json", "w") as f:
            json.dump(users_data, f, indent=4)

    def has_attempts_left(self):
        return self.attempts < self.max_attempts

    def increment_attempts(self):
        self.attempts += 1

    def update_score(self, section, correct_answers, total_questions):
        # Bölüm puanını 100 üzerinden normalize et ve yuvarla
        section_score = round((correct_answers / total_questions) * 100, 2) if total_questions > 0 else 0
        self.success_per_section[section] = section_score
        self.calculate_overall_score()

    def calculate_overall_score(self):
        # Genel puanı tüm bölümlerin ortalaması olarak hesapla ve yuvarla
        total_score = sum(self.success_per_section.values())
        self.score = round(total_score / len(self.success_per_section), 2)

    def get_score(self):
        return round(self.score, 2)  # Genel başarıyı iki ondalıklı olarak döndür
