import phonenumbers
class AnalysisResults:
    def __init__(self):
        self.spelling_error_count=None
        self.grammar_error_count=None
        self.email_suspicious=None
        self.link_suspicious=None
        self.phone_suspicious=None
        self.pay_suspicious=None
        self.ai_analysis=None
        self.ai_summary=None
        self.ai_skills=[]
        self.cumulative_risk=None
    def display(self):
        print("Spelling Error Count:", self.spelling_error_count)
        print("Grammar Error Count:", self.grammar_error_count)
        print("Email Suspicious:", self.email_suspicious)
        print("Link Suspicious:", self.link_suspicious)
        print("Phone Suspicious:", self.phone_suspicious)
        print("Pay Suspicious:", self.pay_suspicious)
        print("AI Analysis:", self.ai_analysis)
        print("AI Summary:", self.ai_summary)
        print("AI Skills:", self.ai_skills)
        print("Cumulative Risk:", self.cumulative_risk)


class ContactInfo:
    def __init__(self, phone_number:str, email, name=None):
        self.name = name
        self.phone_number = phonenumbers.parse(phone_number,"US")
        self.email = email
    def display(self):
        print("Name:", self.name)
        print("Phone Number:", self.phone_number)
        print("Email:", self.email)
        
class Job:
    def __init__(self, domain, link, position_title, description, company, post_date, contact_info:ContactInfo=None):
        self.domain = domain
        self.link = link
        self.position_title = position_title
        self.description = description  # Text
        self.contact_info = contact_info
        self.company = company
        self.post_date = post_date

    def display(self):
        print("Domain:", self.domain)
        print("Link:", self.link)
        print("Position Title:", self.position_title)
        print("Description:", self.description)
        if self.contact_info:
            print("Contact Information:")
            self.contact_info.display()
