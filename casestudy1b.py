# getting the sentence of words

my_sentence = input('please enter a sentence: ')

#split the strings into separating words
split_words = my_sentence.split()

print(split_words)

# sort alphabetically and print
split_words.sort()


for word in split_words:
    print(word)

