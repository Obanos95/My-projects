
def number_differents_characters(text):
    '''
    number of differents characters in a given text.

    :param text: text to analyse
    :type text: str
    :return: number of differents characters
    :type: int
    '''
    assert isinstance(text, str)
    used_chars = []
    dif_chars = 0
    for char in text:
        if char not in used_chars:
            dif_chars += 1
            used_chars.append(char)
    return dif_chars


def number_words(text):
    '''
    number of words in a text.
    
    It is assumed that these are the spaces that allow words to be recognized. 
    The words are between spaces.

    :param text: text to analyse
    :type text: (str)
    :return: number of words in a text
    :type: (int)
    '''
    assert isinstance(text, str)
    words = []
    word = []
    for char in (text + ' '):
        if char != ' ':
            word.append(char)
        else:
            if len(word) != 0:
                words.append(word)
            word = []
    return len(words)


def number_words_differents(text):
    '''
    number of differents words in a text.
    
    It is assumed that these are the spaces that allow words to be recognized. 
    The words are between spaces.

    :param text: text to analyse
    :type text: str
    :return: number of differents words in a text
    :type: (int)
    '''
    assert isinstance(text, str)
    words = []
    word = []
    for char in (text + ' '):
        if char != ' ':
            word.append(char)
        else:
            if len(word) != 0 and word not in words:
                words.append(word)
            word = []
    return len(words)