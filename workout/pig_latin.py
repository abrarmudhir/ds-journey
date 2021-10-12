def pig_latin(word):
    """
    Pig Latin
    :param word:
    :return:
    """
    if word[0] in 'aeiou':
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'
