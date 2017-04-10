def keyword_usage(sentence, words):
    truthtable = []
    sentence = sentence.split()
    for word in words:
        if word in sentence:
            truthtable.append(True)
        else:
            truthtable.append(False)

    truthtable = tuple(truthtable)
    return truthtable


res = keyword_usage('Dive  Into  Python',  ['Python',  'python', 'scala'])
print (res)
