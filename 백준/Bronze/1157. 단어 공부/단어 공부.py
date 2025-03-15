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
    
# 처음 문제 풀이  
# word = input().lower()
# # 글자 개수를 세고 저장
# # 비교를 통한 출력값 설정
# word_set = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'n':0,
#             'm':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
# new_set = {}
# for i in word: # 글자 개수를 세고 저장
#     word_set[i]+=1
    
# for i in word_set: # 0인거 글자는 삭제
#     if word_set[i]!=0:
#         new_set[i] = word_set[i]

# maximum = 0 # 최대값 비교
# max_cnt = 0 # 최대값이 같은게 몇개 있는지
# max_word = '' # 최대 값인 문자 출력
# for key in new_set:
#     if maximum < new_set[key]: # 가장 큰 값 찾기
#         maximum = new_set[key] # maximum에 가장 큰 값 저장
#         max_word = key # max_word에 가장 큰 문자 저장
#         max_cnt = 0 # 예시: {a:2, b:3, c:3, d:4, e:5}, b:3, c:3 구간에서 max_cnt == 2가 되었지만 d:4가 나오면서 max_cnt=0으로 만들면서 초기화  
#     elif maximum == new_set[key]: # maximum == new_set[key]이 같으면 max_cnt +=1 
#         max_cnt += 1
# if max_cnt > 1: # 문자가 최대인 것들이 2개 이상이면 예를들어, {a:4,b:4,c:3} 과 같이 있다면 max_cnt는 2가 되어 ?을 출력
#     print('?')
# else: # 최대값인 문자 대문자로 출력
#     print(max_word.upper())
        