

def designer_pdf_viewer(h, word):
    """

    :param h:  contains 26 space-separated integers describing the respective heights of each consecutive
     lowercase English letter, ascii[a-z].
    :param word: a single word, consisting of lowercase English alphabetic letters
    :return: a single integer denoting the area in mm of highlighted rectangle when the given word is selected
    """
    max_ = 0
    for i in range(len(word)):
        if max_ < h[ord(word[i]) - 97]:
            max_ = h[ord(word[i]) - 97]
    return max_ * len(word)


if __name__ == '__main__':
    """
    1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    abc
    """
    h = list(map(int, input().rstrip().split()))
    word = input()
    result = designer_pdf_viewer(h, word)
    print(result)
