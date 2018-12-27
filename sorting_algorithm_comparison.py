import numpy as np
import timeit

"""比较一下每个算法的时间"""
x = np.arange(10000)
x = np.random.permutation(x)
sort_1 = timeit.Timer("bubble_sort.bubble_sort_1(x.copy())", "from __main__ import x;import bubble_sort")
print("bubble_sort:", sort_1.timeit(number=1), "seconds")
sort_2 = timeit.Timer("selection_sort.selection_sort(x.copy())", "from __main__ import x;import selection_sort")
print("selection_sort:", sort_2.timeit(number=1), "seconds")
sort_3 = timeit.Timer("insertion_sort.insertion_sort(x.copy())", "from __main__ import x;import insertion_sort")
print("insertion_sort:", sort_3.timeit(number=1), "seconds")
sort_4 = timeit.Timer("shell_sort.shell_sort(x.copy())", "from __main__ import x;import shell_sort")
print("shell_sort:", sort_3.timeit(number=1), "seconds")
