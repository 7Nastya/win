# A. Совпадение? Не думаю
alice = list(str(input()).strip())
zeliboba = list(str(input()).strip())
R = []
d = {}
count_alice = len(alice)
count_zelib = len(zeliboba)

for i in range(count_zelib):
    if zeliboba[i] != '1':
        for j in range(count_alice):
            if alice[j] != '1':
                if zeliboba[j] == alice[j]:
                    d[j] = 'P'
                    zeliboba[j] = '1'
                    alice[j] = '1'
                    continue
                if zeliboba[i] == alice[j]:
                    alice[j] = '1'
                    zeliboba[i] = '1'
                    d[i] = 'S'

ans_s = "".join(map(str, alice))
ans_q = "".join(map(str, zeliboba))

for i in range(len(ans_s)):
    if ans_q[i] != '1':
        if ans_q[i] not in ans_s:
            d[i] = 'I'

res = dict(sorted(d.items(), key=lambda x: x[0]))

for k, n in res.items():
    R.append(n)

ans_str = "".join(map(str, R))
print(ans_str)
