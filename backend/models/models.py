class User:
    def __init__(self, email, first_name, last_name, user_id=None, skills=None, industry=None, years_of_experience=None, salary=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.skills = skills
        self.industry = industry
        self.years_of_experience = years_of_experience
        self.salary = salary

class Feedback:
    def __init__(self, email, report_id, feedback):
        self.email = email
        self.report_id = report_id
        self.feedback = feedback