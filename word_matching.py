def match_words(words):
    ctr = 0
    lst = []

    for s in words:
        if len(s) > 1 and s[0] == s[-1]:
            ctr += 1
            lst.append(s)

    print("Lists of words with first and last character same:",lst)
    return ctr

count = match_words(["abc",'sos','cfc','mls','wxyz','loot'])

print("Number of words having first and last character same: ",count)