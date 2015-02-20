"""
Реши задачу и получи награду CodeStars Awards:

Чтобы жюри международного конкурса исполнителей «Еврослух» больше не обвиняли в необъективном судействе,
организаторы конкурса решили внедрить им в помощь автоматическую систему оценки исполнителей.
Эта система автоматически фиксирует правильность исполнения танца по координатам
исходя из попадания в свет софита и подсчет штрафных баллов за ошибки.

Прошлый опыт с треугольными софитами показал себя не очень эффектным,
поэтому светорежиссер поставил обычные, круглые софиты.
При этом если участник конкурса попадает на границу освещения, то система не фиксирует ошибку.

На вход программа получает файл с координатами центров кругов освещения и их радиусов,
в последней строчке — координаты участника конкурса на сцене в этот момент.

Программа должна посчитать количество штрафных баллов,
а также указать в какие круги-диапазоны попал исполнитель (указать строчки во входном файле).
Для расчётов считать размер штрафа за попадание в свет софита с ошибкой — 499 баллов,
сначала выводить все номера диапазонов (номера начинаются с 1), потом — сумму.
Если исполнитель не попал ни в один круг, нужно вывести 0.

Решение:
(x - x0)^2 + (y - y0)^2 <= R^2

где x и y - координаты вашей точки,
x0 и y0 - координаты центра окружности,
R - радиус окружности, ^2 - возведение в квадрат.
"""

with open("92.txt", 'r') as inf:
    data = [list(map(int, line.strip().split())) for line in inf]

point = data.pop()
px = point[0]
py = point[1]

nomer = 0
result = []

d = []
for d in data:
    nomer += 1

    x, y, r = d

    if (x-px)**2 + (y-py)**2 <= r**2:
        result.append(nomer)

if result:
    for res in result:
        print (res, end=' ')
    print (len(result)*499)
else:
    print("0")