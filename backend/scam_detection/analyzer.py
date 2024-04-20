import text_analysis as ta
from job_analysis import *
from contact_analyzer import ContactAnalyzer
import phonenumbers
class Analyzer:
    def __init__(self):
        self.text_analyzer=ta.LangToolAnalyzer()
        self.contact_analyzer=ContactAnalyzer()
    def run_analysis(self,job:Job):
        analysis=AnalysisResults()
        analysis.spelling_error_count,analysis.grammar_error_count\
            =self.text_analyzer.analyze_spelling_and_grammar(job.description)
        
        #Contact analysis stuff
        if(job.contact_info != None):
            analysis.email_suspicious=self.contact_analyzer.email_is_suspicious(job.contact_info.email,job.company)
            analysis.phone_suspicious=self.contact_analyzer.phone_number_is_suspicious(job.contact_info.phone_number)
        else:
            analysis.email_suspicious=None
        return analysis

#Testing data legit
# c=ContactInfo("3303475375","sarah.west@radiancetech.com","sarah west")
# j=Job("www.radiancetech.com","www.radiancetech.com","Budget Analyst","Radiance Technologies, a rapidly growing employee-owned company, is seeking a Journeyman Budget Analyst professional to support the U.S. Army Tactical Exploitation of National Capabilities (TENCAP) program. The successful candidate will apply expertise and working knowledge of DOD financial execution processes and reporting to the budget planning, execution, and reconciliation of all appropriations allocated or provided to the Army TENCAP office. They will analyze historical funding execution data to develop budgets and spend plans that will execute funds in a timely manner, and in accordance with the program's acquisition strategies and OSD standardized goals. The candidate will also generate funding documentation and reports using the internal office database, Standard Operation and Maintenance Army Research and Development Systems (SOMARDS) database, the General Fund Enterprise Business Systems (GFEBS), GFEBS-Sensitive Activities (GFEBS-SA), Logistics Management Program (LMP), Wide Area Workflow (WAWF) and G-Invoice software. Additionally, they will perform all budget phases, i.e., formulation, justification, presentation, and execution; administer the Agency Operating Budget, Mid-Year Review, Budget Execution Review, Year-end Closeout and related budget reports.","Radiance Technologies",c)
# a=Analyzer()
# a.run_analysis(j).display()