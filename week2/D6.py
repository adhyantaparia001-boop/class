def word_frequency(sentence):
    words = {}
    set = sentence.lower().split()
    for item in set :

        if  item in words:
            words[item] += 1
        if item not in words:
            words[item] = 1
    return words
print(word_frequency("hello Hello My name is Devansh Taparia and My brothers name is Adhyan Taparia"))