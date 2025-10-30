import sys

N = int(input())
N_dict = {i:1 for i in list(map(int,input().split()))}
M = int(input())
M_list = list(map(int,input().split()))

for i in M_list:
    try:
        print(N_dict[i])
    except:
        print(0)
