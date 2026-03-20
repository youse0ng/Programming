N = int(input())
book = {}
for _ in range(N):
    name = input()
    if name in book:
        book[name] += 1
    elif name not in book:
        book[name] = 1

maximum = max(book.values())

for key in sorted(book):
    if book[key] == maximum:
        print(key)
        break