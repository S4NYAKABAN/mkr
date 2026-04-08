import re

class TextAnalyzer:
    def read_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()