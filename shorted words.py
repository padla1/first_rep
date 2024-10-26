def find_short(s):
    words = s.split()
    shorted_words = words[0]
    for i in words:
        if len(i)<len(shorted_words):
            shorted_words = i
    return len(shorted_words)







print(find_short("Lets all go on holiday somewhere very cold"))
