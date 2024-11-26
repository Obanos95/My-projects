
def number_differents_characters(text):
    '''
    number of differents characters in a given text.

    :param text: text to analyse
    :type text: str
    :return: number of differents characters
    :type: int
    '''
    assert isinstance(text, str)
    dif_char_num = 0
    used_char = []
    for i in text:
        if i not in used_char:
            dif_char_num += 1
            used_char.append(i)
    return dif_char_num


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
    words_num = 0
    word = []
    #for i in text:
    #    if i != ' ':



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
    pass
