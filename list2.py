def match_words(words):
    ctr = 0
    lst = []
    for words in words:
        if len(words) > 1 and words[0] == words[-1]:
            lst.append(words)
            ctr += 1

    print("the list of number with first character and last character are same ",lst)
    return ctr

count = match_words(['abc', 'cfc', 'xyz', 'aba', '1221'])
print("the count of number in which first character and last character are same ",count)