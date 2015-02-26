"""
В новой версии Монструс Креативус 3500 для написания музыкальных шедевров
использует более продвинутый язык программирования !++.
К командам !# добавляются более сложные команды:

• $ - поменять местами два верхних элемента стека

• @ - дублировать верхний элемент стека

• - - уменьшить верхушку стека на 1

• [ - установить метку в программе

• < - если верхушка стека не равна 0,
    то возврат на последнюю метку в программе
    (верхушка стека при этом удаляется),
    иначе – продолжение выполнения программы

• ` - удалить верхний элемент стека

Во входном файле содержится программа на языке !++.
Определи, что напечатает эта программа. Возможно, это уже настоящий хит.
"""

with open('data/12.data', 'r') as inf:
    for str in inf:
        s = str

alfavit = "abcdefghijklmnopqrstuvwxyz"
result = ''

stack = []
stack.append(10)
sss = stack.pop()

# for i in range(len(s)):
i = 0
while i < len(s):
    c = s[i]
    if c == 'Z':
        stack.append(0)
    elif c == '+':
        stack.append(stack.pop() + stack.pop())
    elif c == '*':
        stack.append(stack.pop() * stack.pop())
    elif c == '!':
        result += alfavit[stack.pop()]
    elif c == '#':
        stack.append(stack.pop() + 1)
    elif c == '%':
        pass
    elif c == '~':
        result += ' '
    elif c == '$':
        e1 = stack.pop()
        e2 = stack.pop()
        stack.append(e1)
        stack.append(e2)
    elif c == '@':
        e = stack.pop()
        stack.append(e)
        stack.append(e)
    elif c == '-':
        stack.append(stack.pop() - 1)
    elif c == '[':
        metka = i
    elif c == '<':
        e = stack.pop()
        if e != 0:
            i = metka
        # else:
        #     stack.append(e)
    elif c == "`":
        stack.pop()
    i += 1

print(result)
