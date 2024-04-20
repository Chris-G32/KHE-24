import language_tool_python as lang
import re
def tokenize_text(text:str)->list[str]:
    pattern="\w+|[^\w\s],+"
    words=re.findall(pattern,text)
    return words

#This can analyze the grammar and spelling of a given text string, currently unsure of how performant it is on large text.
class LangToolAnalyzer:
    def __init__(self, language="en-US"):
        self.lang_tool=lang.LanguageTool(language)
    def analyze_spelling_and_grammar(self, text: str):
        def is_grammar_error(item):
            return item.ruleIssueType=='grammar'
        def is_spelling_error(item):
            return item.ruleIssueType=='misspelling'
        results=self.lang_tool.check(text)
        grammar_issues=list(filter(is_grammar_error,results))
        spelling_issues=list(filter(is_spelling_error,results))
        return (len(spelling_issues),len(grammar_issues)) 
    
