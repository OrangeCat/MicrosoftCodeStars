"""
Спеть со звездой – настоящая удача для начинающего исполнителя!
Но неужели твое имя будет стоять вторым на диске, плакатах…
Твое честолюбие не позволит этому случиться, ведь ты уже в шаге от статуса суперзвезды!
Кажется, конфликт неизбежен. Чтобы споры за первенство не поставили крест на совместной работе,
звукоинженер предложил определить, сколько работы вложил каждый из исполнителей в песню.
Твои партии в записи он пометил буквами x,y,z,w, а партии приглашенной звезды - a,b,c,d.
Также в расшифровке записи присутствуют другие случайные символы, обозначающие партии бэк-вокала, которые можно игнорировать.
Принадлежность к конкретному исполнителю тем сильнее, чем длиннее максимальная подпоследовательность партии этого исполнителя.

Давай узнаем, чье же имя окажется первым – определи на сколько процентов песня твоя.
"""

myletters = {'x','y','z','w'}
altletters = {'a','b','c','d'}
s = ''

with open('106.data', 'r', encoding="utf-8") as inf:
    for st in inf:
        s = st

mlen_max = 0
alen_max = 0

mlen = 0
alen = 0

for c in s:
    if c in myletters:
        mlen += 1
        if alen > 0:
            alen_max = max(alen_max, alen)
            alen = 0
    elif c in altletters:
        alen += 1
        if mlen > 0:
            mlen_max = max(mlen_max, mlen)
            mlen = 0

print (mlen_max/(mlen_max+alen_max)*100)