i = -1
print("Здравствуйте! Эта программа проверяет правильность следующего утверждения "
      "для введенной скобочной последовательности:")
print("Правильная скобочная запись с двумя видами скобок. "
      "Внутри квадратной скобки должна быть хотя бы одна квадратная либо ничего")
print("Примеры правильных последовательностей: \n[()([]([]()()))]\n[()[]]\n[([()])]\n(())")
errors = 0


def read():
    global i
    i += 1
    if i == len(s):
        return 0
    else:
        return s[i]


def error():
    global errors
    errors = 1


def chain(symb):
    if (symb == '['):
        symb = read()
        symb = chain1(symb)
        if (symb == ']'):
            symb = read()
        else:
            error()
        symb = chain(symb)
    elif (symb == '('):
        symb = read()
        symb = chain(symb)
        if (symb == ')'):
            symb = read()
        else:
            error()
        symb = chain(symb)
    return symb


def chain1(symb):
    if (symb == '['):
        symb = read()
        symb = chain2(symb)
        if (symb == ']'):
            symb = read()
        else:
            error()
        symb = chain(symb)
    elif (symb == '('):
        symb = read()
        symb = chain1(symb)
        if (symb == ')'):
            symb = read()
        else:
            error()
        symb = chain(symb)
    elif (symb == ']'):
        symb = chain2(symb)
    else:
        error()
    return symb

def chain2(symb):
    if (symb == '[' or symb == '('):
        symb = chain1(symb)
    return symb


flag = True

while (flag):
    print("Пожалуйста, введите строку и по окончании нажмите Enter")
    s = input()
    symb = read()
    symb = chain(symb)
    if (symb == 0 and errors == 0):
        print("Все верно!")
    else:
        print("Ошибка!")
    print("Хотите попробовать снова? 1 - Да, 0 - Нет")
    flag = -1
    while flag not in [True, False]:
        f = input()
        if len(f) == 1:
            flag = bool(int(f))
            if flag not in [True, False]:
                print("Вы ввели некорректный ответ. Повторите попытку")
        else:
            print("Вы ввели некорректный ответ. Повторите попытку")
    if (flag == False):
        break
    i = -1
    errors = 0

