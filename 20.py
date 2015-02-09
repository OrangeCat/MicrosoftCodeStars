"""
Сенсационное открытие сделали недавно британские астрофизики:
 на других планетах не только есть жизнь, но и своя поп-культура!
 Анализируя полученные сообщения с радиотелескопа
 (одно из них дается вам в качестве задания) они обнаружили
 фрагменты ритуальных песен инопланетян!

Установлено, что в песнях очень часто повторяются похожие пары слов
(например, «hey сortana» или “ok google” – будем называть их значимыми парами),
перемежаемые большим количеством слов, не поддающихся расшифровке.
Для общения с инопланетянами предлагается послать им обратно послание, с
обранное из значимых пар следующим образом:
берем в порядке убывания частоты все первые слова пар,
и для каждого такого слова в качестве второго берем самое часто встречающееся
из вторых слов для данного первого слова.
Полученные слова надо записать подряд в виде единого
текста для передачи на радиотелескоп.

Вам предлагается написать такую программу для генерации ответного послания. Удачи!
"""
from operator import itemgetter

def max_count_world(lst):
    c=0
    w=''
    #lst = sorted(lst)
    for i in range(len(lst)):
        ww = lst[i]
        cc = lst.count(ww)
        if cc > c:
            c = cc
            w = ww

    return w

d = {}
r = ""
r2 = ""
r3 = ""
with open("101.data", 'r') as inf:
    for line in inf:
        data = line.strip()

s = data.split()

# Определим значимые пары
for i in range(len(s)-1):
    ps = s[i]+' '+s[i+1]
    if ps not in d:
        if data.count(ps)>1:
            d.update({ps: data.count(ps)})

d = sorted(d.items(), key=itemgetter(1), reverse=True)
print(d)

d2 = {}
ds = []
for i in range(len(d)):
    first, second = d[i][0].split()
    if first in d2:
        d2[first].append(second)
    else:
        d2.update({first: [second]})
        #ds.append(first)
ds = sorted([[k,len(v)] for k,v in d2.items()], key=itemgetter(1), reverse=True)
print(ds)
ds = [ds[i][0] for i in range(len(ds)) ]
print(ds)

for i in range(len(ds)):
    r+= ds[i] + max_count_world(d2[ds[i]])
    r2+= ds[i] + max_count_world(d2[ds[i]]) + " "
    r3+= ds[i] + " " + max_count_world(d2[ds[i]]) + " "

print(r)
print(r2)
print(r3)
#l = sorted(d.items(), key=itemgetter(1), reverse=True)

#print(max_count_world(['aaa', 'bbb', 'ccc', 'bbb']))