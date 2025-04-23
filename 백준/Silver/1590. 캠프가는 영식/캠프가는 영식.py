N, arrival_time = map(int,input().split())
result = []
for _ in range(N):
    start_time, interval_time, buses = map(int,input().split())
    next_time = 0
    times = 1
    if arrival_time == start_time:
        print(0)
        break
    elif arrival_time > start_time:
        next_time = start_time
        while times < buses and next_time <= arrival_time:
            next_time += interval_time
            times += 1
            if next_time - arrival_time >= 0:
                result.append(next_time - arrival_time)
    else:
        result.append(start_time - arrival_time)
else:
    if not len(result):
        print(-1)
    else: 
        print(min(result))