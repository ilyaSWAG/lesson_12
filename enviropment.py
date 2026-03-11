def ddct(res, line):
        res[line[0]] = res.get(line[0], line[1:len(line)])

n = int(input())
res = {}
for i in range(n):
    ddct(res, input().split())
    
m = int(input())

print("default")

for i in range(m):
    a = input()
    for key in res.keys():
        if a in res[key]:
            print(key)







def property(line, path):
    s = 0
    while line < path:
        line += 1
        s += 1
    return f"{s} количество шагов"







print(property(3, 12))

