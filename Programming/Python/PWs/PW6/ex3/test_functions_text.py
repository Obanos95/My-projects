from functions_text import *

def test_number_differents_characters():
    assert 4 == number_differents_characters('hello') # I changed assert 6 to assert 4 because there are only 4 different characters in the word
    assert 1 == number_differents_characters('ooooooooooo')
    assert 2 == number_differents_characters('abaabaabaabaaba')
    assert 0 == number_differents_characters('')


def test_number_words():
    assert 3 == number_words('simple text here')
    assert 3 == number_words('how many words?') # I changed assert 4 to assert 3 because there are only 3 words in the text
    assert 7 == number_words(' a b c   d   e f g ')
    assert 7 == number_words(' a b c   d   a b c ')
    assert 0 == number_words('')

def test_number_words_differents():
    assert 3 == number_words_differents('simple text here')
    assert 3 == number_words_differents('how many words?') # I changed assert 4 to assert 3 because there are only 3 different words in the text
    assert 3 == number_words_differents('dog cat bird') # I changed assert 4 to assert 3 because there are only 3 different words in the text
    assert 7 == number_words_differents(' a b c   d   e f g ')
    assert 4 == number_words_differents(' a b c   d   a b c ')
    assert 0 == number_words_differents('')

test_number_differents_characters()
test_number_words()
test_number_words_differents()