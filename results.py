class Result:
    def __init__(self):
        self.section_scores = {}
        self.overall_score = 0

    def calculate_section_scores(self, section_id, correct_answers, total_questions):
        if total_questions == 0:
            score = 0
        else:
            score = (correct_answers / total_questions) * 100
        self.section_scores[section_id] = round(score, 2)
        return self.section_scores[section_id]

    def get_section_score(self, section_id):
        return self.section_scores.get(section_id, 0)

    def calculate_overall_score(self):
        if self.section_scores:
            total_score = sum(self.section_scores.values())
            self.overall_score = round(total_score / len(self.section_scores), 2)
        return self.overall_score
