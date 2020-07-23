#entering a word or phrase and finding the number of letters and digits. 

# inputting hte sentence 

my_sentence = input('enter a word or phrase: ')


d = 0 
l = 0 

for i in my_sentence:
    if(i.isdigit()):
        d = d + 1
    elif i.isalpha():
        l = l + 1
    else:
        pass
    
print('letters: ', l)
print("numbers ", d)
