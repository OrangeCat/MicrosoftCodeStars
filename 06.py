"""
Билет на твой первый концерт в Лужниках содержит 8 цифр от 0 до 4.
Чтобы увеличить прибыль, перекупщики придумали понятие обобщенно-счастливого билета.
Обобщенно-счастливым называется билет, номер которого можно разбить на две части таким образом, чтобы сумма цифр обеих частей совпадала.
Сколько всего таких билетов?
"""

l = 8
v = 4+1
c = [0 for i in range(l)]
n = 0


# for j in range (l-1, -1, -1):
#     jj = j
#     for i in range(v):
#         c[jj]=i
#         print(c)

# Генерация номеров билетов
# пока немного говнокода
for c[0] in range(v):
    for c[1] in range(v):
        for c[2] in range(v):
            for c[3] in range(v):
                for c[4] in range(v):
                    for c[5] in range(v):
                        for c[6] in range(v):
                            for c[7] in range(v):
                                # Проверка условия задачи
                                for iz in range(l):
                                    s1=0
                                    s2=0
                                    for jz in range(iz):
                                        s1 += c[jz]
                                    for jz in range(iz, l):
                                        s2 += c[jz]
                                    if s1==s2:
                                        n+=1
                                        break
print(n)

# Ответ 78125