from spellchecker import SpellChecker
import re
        
def tokenize_text(text:str)->list[str]:
    pattern="\w+|[^\w\s],+"
    words=re.findall(pattern,text)
    return words

def analyze_spelling(inp:str):
    words=tokenize_text(inp)
    sp = SpellChecker()
    unknown=sp.unknown(words)
    return (len(unknown),len(words))
