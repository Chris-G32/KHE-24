from job_analysis import ContactInfo
import re
from phonenumbers import PhoneNumber,parse

class ContactAnalyzer:
    def __init__(self) -> None:
        pass
    
    def email_is_suspicious(self,email:str,company_name:str):
        def sanitize_company_name(name):
            return re.sub(r'[,\']', '', name)
        #Check if known in db
        #if known return false, else run the following
        email=email.lower()
        company_name=sanitize_company_name(company_name).lower()
        company_elements=company_name.split(' ')
        #Analyze email manually
        split=email.split('@')
        user=split[0]
        domain=split[1]

        #Check if domain is suspicious
        any_element_in_domain=False
        for element in company_elements:
            if(domain.find(element)!=-1):
                any_element_in_domain=True
        
        return not any_element_in_domain
    

    def phone_number_is_suspicious(self,phone_number:PhoneNumber):
        return phone_number.country_code != 1 