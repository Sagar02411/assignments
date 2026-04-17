def count_words(sentence):
    words = sentence.split()
    return len(words)# Bug here
print(count_words('this is a sentence  '))