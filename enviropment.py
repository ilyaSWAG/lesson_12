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



def money(a, b):
    return a + b



print(money(3, 55))




def solutions():
     print("commits")


for i in range(4):
     solutions()

print("summ")