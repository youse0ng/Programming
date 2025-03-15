word = input().lower()
# 글자 개수를 세고 저장
# 비교를 통한 출력값 설정
word_set = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'n':0,
            'm':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
new_set = {}
for i in word: # 글자 개수를 세고 저장
    word_set[i]+=1
    
for i in word_set: # 0인거 글자는 삭제
    if word_set[i]!=0:
        new_set[i] = word_set[i]

maximum = max(new_set.values()) # 최대값 비교
max_cnt = 0 # 최대값이 같은게 몇개 있는지
max_word = '' # 최대 값인 문자 출력

for key in new_set:
    if maximum == new_set[key]:
        max_cnt += 1
        max_word = key
if max_cnt > 1:
    print('?')
else:
    print(max_word.upper())