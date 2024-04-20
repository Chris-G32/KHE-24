import text_analysis as ta
from job_analysis import *
class Analyzer:
    def __init__(self):
        self.text_analyzer=ta.LangToolAnalyzer()
    def run_analysis(self,job:Job):
        analysis=AnalysisResults()
        analysis.spelling_error_count,analysis.grammar_error_count\
            =self.text_analyzer.analyze_spelling_and_grammar(job.description)
        return analysis