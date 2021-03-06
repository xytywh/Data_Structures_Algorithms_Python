import timeit


def t_1():
    li = []
    for i in range(10000):
        li.append(i)


def t_2():
    li = []
    for i in range(10000):
        li.insert(0, i)


def t_3():
    li = []
    for i in range(10000):
        li += [i]


# t_3和t_4不会创建新对象，t_5会创建一个新对象，t_3比t_4快得多。

def t_4():
    li = []
    for i in range(10000):
        li.extend([i])


def t_5():
    li = []
    for i in range(10000):
        li = li + [i]


def t_6():
    li = [i for i in range(10000)]


def t_7():
    li = list(range(10000))


timer1 = timeit.Timer("t_1()", "from __main__ import t_1")
print("append:", timer1.timeit(1000))
timer2 = timeit.Timer("t_2()", "from __main__ import t_2")
print("insert:", timer2.timeit(1000))
timer3 = timeit.Timer("t_3()", "from __main__ import t_3")
print("+=:", timer3.timeit(1000))
timer4 = timeit.Timer("t_4()", "from __main__ import t_4")
print("extend:", timer4.timeit(1000))
timer5 = timeit.Timer("t_5()", "from __main__ import t_5")
print("= +:", timer5.timeit(1000))
timer6 = timeit.Timer("t_6()", "from __main__ import t_6")
print("[i for i in range]:", timer6.timeit(1000))
timer7 = timeit.Timer("t_7()", "from __main__ import t_7")
print("list(range():", timer7.timeit(1000))

x = list(range(2000000))
pop_zero = timeit.Timer("x.pop(0)", "from __main__ import x")
print("pop_zero ", pop_zero.timeit(number=1000), "seconds")
x = list(range(2000000))
pop_end = timeit.Timer("x.pop()", "from __main__ import x")
print("pop_end ", pop_end.timeit(number=1000), "seconds")
# pop最后一个元素的效率远远高于pop第一个元素
