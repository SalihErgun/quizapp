class Result:
    def __init__(self):
        """
        Initializes the Result object with dictionaries to store section scores
        and the overall score.
        """
        self.section_scores = {}  # Dictionary to store scores per section
        self.overall_score = 0    # Total score for the entire exam

    def calculate_section_scores(self, section_id, correct_answers, total_questions):
        """
        Calculates the score for a particular section and stores it in section_scores.
        
        Parameters:
            section_id (str): The identifier for the section (e.g., "section1").
            correct_answers (int): Number of questions answered correctly in this section.
            total_questions (int): Total number of questions in this section.
        
        Returns:
            float: The percentage score for the section.
        """
        if total_questions > 0:
            section_score = (correct_answers / total_questions) * 100
        else:
            section_score = 0
        
        self.section_scores[section_id] = section_score
        return section_score

    def calculate_overall_score(self):
        """
        Calculates the overall score based on the scores of each section and
        stores it in the overall_score attribute.
        
        Returns:
            float: The overall percentage score across all sections.
        """
        if self.section_scores:
            total_score = sum(self.section_scores.values())
            self.overall_score = total_score / len(self.section_scores)
        else:
            self.overall_score = 0
        
        return self.overall_score

    def display_results(self):
        """
        Displays the scores for each section and the overall score.
        Indicates whether the user passed or failed based on a passing score of 75%.
        """
        print("----- Exam Results -----")
        for section_id, score in self.section_scores.items():
            print(f"{section_id.capitalize()} Score: {score:.2f}%")
        
        print(f"Overall Score: {self.overall_score:.2f}%")
        
        # Determine pass/fail status based on a 75% passing score
        if self.overall_score >= 75:
            print("Status: Passed")
        else:
            print("Status: Failed")

    def get_pass_fail_status(self):
        """
        Checks if the overall score meets the passing criteria.
        
        Returns:
            bool: True if the overall score is 75% or above, False otherwise.
        """
        return self.overall_score >= 75
