# a, b = input().split()
# print(int(a) + int(b))
# with 'input.txt' as f:
c = {}
c[1] = 1
c['1'] = 2
c[1] += 1
s = 0
for k in c:
    s += c[k]
print(s)