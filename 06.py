"""
Билет на твой первый концерт в Лужниках содержит 8 цифр от 0 до 4.
Чтобы увеличить прибыль, перекупщики придумали понятие обобщенно-счастливого билета.
Обобщенно-счастливым называется билет, номер которого можно разбить на две части таким образом, чтобы сумма цифр обеих частей совпадала.
Сколько всего таких билетов?
"""

l = 8 # Кол-во цифр в номере билета
v = 4 # Каждая цифра от 0 до v
c = [0 for i in range(l)]
r = [v for i in range(l)]
n = 0

# Генерация номеров билетов
while c != r:
    for j in range(l):
        allV = True
        for i in range(j, l):
            if c[i] != v:
                allV = False
                break
        if allV:
            c[j - 1] += 1
            for i in range(j, l):
                c[i] = 0
    for i in range(v + 1):
        c[l - 1] = i
        print(c)
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