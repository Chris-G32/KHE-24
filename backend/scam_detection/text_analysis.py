from spellchecker import SpellChecker
import language_tool_python as lang
import re
def tokenize_text(text:str)->list[str]:
    pattern="\w+|[^\w\s],+"
    words=re.findall(pattern,text)
    return words

class GrammarAnalyzer:
    def __init__(self,language="en-US"):
        self.lang_tool=lang.LanguageTool(language)
    def analyze_grammar(self,text:str):
        def is_grammar_error(item):
            return item.ruleIssueType=='grammar'
        results=self.lang_tool.check(text)
        filtered=list(filter(is_grammar_error,results))
        return filtered
class SpellingAnalyzer:
    def __init__(self,language="en"):
        self.spellchecker=SpellChecker(language)
    def analyze_spelling(self,text:str):
        words=tokenize_text(text)
        unknown=self.spellchecker.unknown(words)
        return (len(unknown),len(words))
class TextAnalysisTool:
    def __init__(self):
        self.grammar_checker=GrammarAnalyzer()
        self.spell_checker=SpellingAnalyzer()
    def check_spelling_errors(self,text:str):
        return self.spell_checker.analyze_spelling(text)
    def check_grammar_errors(self,text:str):
        return self.grammar_checker.analyze_grammar(text)


# def analyze_spelling(text:str):
#     words=tokenize_text(text)
#     sp = SpellChecker()
#     unknown=sp.unknown(words)
#     return (len(unknown),len(words))

# def analyze_grammar(text:str):
#     def is_grammar_error(item):
#         return item.ruleIssueType=='grammar'
#     tool=lang.LanguageTool("en-US")
#     results=tool.check(text)
#     filtered=list(filter(is_grammar_error,results))
#     return filtered

tool=AnalysisTool()
text="I is chris. htis is my real! job posting."
print(tool.check_grammar_errors(text))
print(tool.check_spelling_errors(text))