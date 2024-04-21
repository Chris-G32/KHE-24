import scam_detection.text_analysis as ta
from scam_detection.job_analysis import *
from scam_detection.contact_analyzer import ContactAnalyzer
import phonenumbers
import scam_detection.ai_analyzer as ai_analyzer
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
            analysis.email_suspicious=False
            analysis.phone_suspicious=False
            
        # AI Analysis
        summary, risk = ai_analyzer.generate_GPT(job.description)
        analysis.ai_summary = summary
        analysis.ai_analysis = risk 

        analysis.cumulative_risk = self.calculate_final_risk(analysis)
        return analysis
    
    def calculate_final_risk(self, report:AnalysisResults):
        flag_gc = report.grammar_error_count > 3
        flag_sc = report.spelling_error_count > 3

        if (report.ai_analysis.lower() == "very low"):
            return report.ai_analysis
        
        if (report.ai_analysis.lower() == "low"):
            temp = 0.5 + 0.05(report.link_suspicious + report.phone_suspicious) + 0.1(report.email_suspicious) + 0.20(flag_gc) + 0.10(flag_sc)
            if   (temp < 0.51):  return "Very low"
            elif (temp < 0.75):  return report.ai_analysis
            else: return "Medium"
        
        if (report.ai_analysis.lower() == "medium"):
            temp = 0.3 + 0.05(report.link_suspicious + report.phone_suspicious) + 0.2(report.email_suspicious) + 0.20(flag_gc) + 0.10(flag_sc)
            if   (temp < 0.5):  return "Medium"
            else: return "High"

        if (report.ai_analysis.lower() == "high"): 
            return report.ai_analysis  

#Testing data legit
# c=ContactInfo("3303475375","sarah.west@radiancetech.com","sarah west")
# j=Job("www.radiancetech.com","www.radiancetech.com","Budget Analyst","Radiance Technologies, a rapidly growing employee-owned company, is seeking a Journeyman Budget Analyst professional to support the U.S. Army Tactical Exploitation of National Capabilities (TENCAP) program. The successful candidate will apply expertise and working knowledge of DOD financial execution processes and reporting to the budget planning, execution, and reconciliation of all appropriations allocated or provided to the Army TENCAP office. They will analyze historical funding execution data to develop budgets and spend plans that will execute funds in a timely manner, and in accordance with the program's acquisition strategies and OSD standardized goals. The candidate will also generate funding documentation and reports using the internal office database, Standard Operation and Maintenance Army Research and Development Systems (SOMARDS) database, the General Fund Enterprise Business Systems (GFEBS), GFEBS-Sensitive Activities (GFEBS-SA), Logistics Management Program (LMP), Wide Area Workflow (WAWF) and G-Invoice software. Additionally, they will perform all budget phases, i.e., formulation, justification, presentation, and execution; administer the Agency Operating Budget, Mid-Year Review, Budget Execution Review, Year-end Closeout and related budget reports.","Radiance Technologies",c)
# a=Analyzer()
# a.run_analysis(j).display()