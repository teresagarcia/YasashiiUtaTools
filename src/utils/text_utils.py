import re

def clean_text(*text):
    test_re = '[^A-Za-z0-9]+'
    keywords = []
    [keywords.append(re.sub(test_re, '', word).lower()) for word in text]
    return keywords