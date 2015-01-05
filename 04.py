"""
На международном музыкальном фестивале участники говорят на множестве разных языков.
Чтобы все могли понимать друг друга, организаторы предложили использовать автоматические переводчики, но переводчики есть не для всех пар языков.
В текстовом файле в каждой строке содержится (через пробел) имя переводчика, с какого языка и на какой он может переводить.
Какое минимальное количество переводчиков необходимо, чтобы переводить с Исландского на Албанский?
"""
l = list() #Список, содержащий пары языков.
d = set()
d2 = set()
n = 0 #Уровень.

with open('24.data', 'r', encoding="utf-8") as inf:
    for s in inf:
        l.append([s.split()[1], s.split()[2]])

f = 'Исландский'
t = 'Албанский'

d.add(f)

while 1==1:
    d2.clear()
    for z in l:
        if z[0] in d:
            d2.add(z[1])
    d.update(d2)
    n += 1
    if t in d:
        break

print (n)