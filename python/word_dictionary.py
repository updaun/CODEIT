word_dict = {}
eng_text = ''
while True:
    eng_text = input("영어 단어를 입력하세요: ")
    if eng_text == 'q':
        break
    word_dict[eng_text] = ''
    kor_text = input("한국어 뜻을 입력하세요: ")
    if kor_text == 'q':
        break
    word_dict[eng_text] = kor_text

#print(word_dict)

with open("./codeit/vocabulary.txt", 'a', encoding="UTF-8") as f:
    for k,v in word_dict.items():
        f.write(f'{k}: {v}\n')

# 모범 답안
# with open('vocabulary.txt', 'w') as f:
#     while True:
#         english_word = input('영어 단어를 입력하세요: ')    
#         if english_word == 'q':
#             break
        
#         korean_word = input('한국어 뜻을 입력하세요: ')
#         if korean_word == 'q':
#             break
        
#         f.write('{}: {}\n'.format(english_word, korean_word))