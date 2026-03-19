N, M = map(int,input().split()) # 저장된 사이트 주소 수 | 찾으려는 주소 수
website_dict = {}
for _ in range(N):
    website, password = input().split()
    website_dict[website] = password
    
for _ in range(M):
    finding = input()
    print(website_dict[finding])