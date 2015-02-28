"""
Твой следующий хит уже на подходе, он будет выпущен буквально на днях.

Крутой журнал Growing Stones попросил у тебя демо этого релиза,
чтобы первыми написать рецензию на него.
Наконец, ты получаешь по электронной почте письмо от главного редактора,
но вот беда:
в тексте автор заменил все буквы на другие буквы,
а остальные знаки оставили без изменений, чтобы конкуренты не могли
украсть его мнение.
Также он приложил к письму файл, представляющий собой частотный словарь
исходного текста, т.е. перечень букв в порядке убывания частоты
их появления в тексте.
Первая строчка входного файла содержит частотный словарь
(символы латинского алфавита в порядке убывания частоты,
возможно, менее 26-ти, если некоторые буквы в файле не встречались),
остальные строчки – сам текст статьи.
Расшифруй текст рецензии, сохранив все знаки препинания.
"""

from operator import itemgetter  # multiple levels of sorting

alfavit = "abcdefghijklmnopqrstuvwxyz"

i = 0
with open('data/10.data', 'r') as inf:
    for str in inf:
        if i == 0:
            s1 = str  # Частотный словарь
            i += 1
        if i == 1:
            s2 = str  # Текст статьи

d = {}   # Здесь соберу частоту встречания каждой буквы
dl = []  # а здесь буквы в порядке их появления/
# Это важно так как есть буквы с одинаковым кол-вом появления в тексте.
for c in s2:
    if c not in alfavit:
        continue
    if c not in d:
        d[c] = 1
        dl.append([c, 0])
    else:
        d[c] += 1

for zn in dl:
    zn[1] = d[zn[0]]

dl = sorted(dl, key=itemgetter(1), reverse=True)

dt = {}  # словарь для перевода
for i in range(min(len(dl), len(s1))):
    dt[dl[i][0]] = s1[i]

result = ''
for c in s2:
    if c in dt:
        result += dt[c]
    else:
        result += c

print(result)
