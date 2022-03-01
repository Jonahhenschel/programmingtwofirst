import random
def get_word():
    key_words=['world','aroma','watch','funny','phone']
    choice=input('would you like to add a word for a friend or no? type Y to add or N to stay')
    if choice=='Y':
        key_words=add_word(key_words)

    random_index=random.randint(0,len(key_words))
    return key_words[random_index]



    
def add_word(key_words):
    possible_word=input('enter a five letter word')
    while check_word(possible_word):
        print('thats not a five letter word!')
        possible_word = input('enter a five letter word')


    key_words.append(possible_word)
    return key_words
def enter_word():
    guess=input('enter a five letter word please!')
    return guess
def check_word(word):
    return len(word)!=5


def wordle():
    chosen_word=get_word()
    guess= enter_word()
    while guess != chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i]==guess[i]:
                print (chosen_word[i] + ' was correct')
            elif guess[i] in chosen_word:
                print(guess[i] + ' in the word but in the wrong spot!')
            else:
                print('sorry ' + guess[i] + ' is not in the word')
        guess=enter_word()
    print('nice!')
wordle()
