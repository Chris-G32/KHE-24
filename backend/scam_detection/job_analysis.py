class AnalysisResults:
    def __init__(self):
        self.spelling_error_count=None
        self.grammar_error_count=None
        self.email_suspicious=None
        self.link_suspicious=None
        self.phone_suspicious=None
        self.ai_analysis=None
        self.ai_summary=None
        self.ai_skills=[]
        self.cumulative_risk=None

class ContactInfo:
    def __init__(self, phone_number, email, name=None):
        self.name = name
        self.phone_number = phone_number
        self.email = email
    def display(self):
        print("Name:", self.name)
        print("Phone Number:", self.phone_number)
        print("Email:", self.email)
        
class Job:
    def __init__(self, domain, link, position_title, description, contact_info=None):
        self.domain = domain
        self.link = link
        self.position_title = position_title
        self.description = description  # Text
        self.contact_info = contact_info

    def display(self):
        print("Domain:", self.domain)
        print("Link:", self.link)
        print("Position Title:", self.position_title)
        print("Description:", self.description)
        if self.contact_info:
            print("Contact Information:")
            self.contact_info.display()
