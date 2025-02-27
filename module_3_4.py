def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if word.lower() in root_word.lower() or root_word.lower() in word.lower():
            same_words.append(word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words('Got', 'forget')
result4 = single_root_words('Got', 'Forgot')
result5 = single_root_words('SnOwMAN', 'snow', 'doctor')
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)