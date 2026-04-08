import pytest
import os
from main import TextAnalyzer

@pytest.fixture
def analyzer():
    return TextAnalyzer()

@pytest.fixture
def temp_file(tmp_path):
    # Створює тимчасовий файл для тесту читання
    f = tmp_path / "test.txt"
    f.write_text("Hello world! This is a test.", encoding="utf-8")
    return str(f)

def test_read_file(analyzer, temp_file):
    assert analyzer.read_file(temp_file) == "Hello world! This is a test."

@pytest.mark.parametrize("text, expected_words", [
    ("Привіт, світ: тест; ок", 4),
    ("Одне слово", 1),
    ("", 0),
    ("Слово , : ; слово", 2)
])
def test_count_words(analyzer, text, expected_words):
    assert analyzer.count_words(text) == expected_words

@pytest.mark.parametrize("text, expected_sentences", [
    ("Це речення. А це? Ого!", 3),
    ("Щось... мабуть.", 2),
    ("Просто текст без крапок", 1),
    ("", 0)
])
def test_count_sentences(analyzer, text, expected_sentences):
    assert analyzer.count_sentences(text) == expected_sentences