import re

class TextAnalyzer:
    def read_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()

    def count_words(self, text):
        # Розділювачі: кома, пробіл, двокрапка, крапка з комою
        words = re.split(r'[ ,:;]+', text)
        return len([w for w in words if w.strip()])