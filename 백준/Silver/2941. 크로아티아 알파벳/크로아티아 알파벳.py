N = input()
for word in ['c=','c-','dz=','d-','lj','nj','s=','z=']:
    try:
        N = N.replace(word,'_')
    except:
        pass
print(len(N))