WORDS=[]
def load_data():
    with open('words_bank.txt','r') as f:
        big_txt=f.read()
        lines=big_txt.split('\n')
        for i in range(0,len(lines),2):
            WORDS.append({'english':lines[i],'persian':lines[i+1]})

def english_to_persian():
    user_txt=input('Enter text english:')
    user_words=user_txt.split(' ')
    output_txt=''
    for user_word in user_words:
        for word in WORDS:
            if user_word==word['english']:
                output_txt +=word['persian']+' '
                break
        else:
            output_txt +=user_word+' '
    print(output_txt) 


def persian_to_english():
    user_txt=input('Enter text persian:')
    user_words=user_txt.split(' ')
    output_txt=''
    for user_word in user_words:
        for word in WORDS:
            if user_word==word['persian']:
                output_txt +=word['english']+' '
                break
        else:
            output_txt +=user_word+' '
    print(output_txt) 


def add_word():
    word=input('Enter new word: ')
    for i in range(len(WORDS)):
      if word==WORDS[i]['english']:
          print('word tekrari')
          break
    else:
        translate=input('Enter word translate: ')
        WORDS.append({'english':word,'persian':translate})
        f=open('words_bank.txt','a')
        f.write('\n'+ word)
        f.write('\n'+ translate)    


load_data()
while True:
    print('1-english to persian ')
    print('2-persian to english')
    print('3-add word')
    print('4-exit')
    choice=int(input('Enter choice:'))

    if choice==1:
        english_to_persian()
    if choice==2:
        persian_to_english()    
    if choice==3:
        add_word()
    if choice==4:
        exit()        