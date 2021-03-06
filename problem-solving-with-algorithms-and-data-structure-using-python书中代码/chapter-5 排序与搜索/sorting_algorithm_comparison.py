import numpy as np
import timeit

"""比较一下每个算法的时间"""
x = np.arange(10000000)
# 数字个数还不够多，所以只是简单的比较一下
x = np.random.permutation(x)
# sort_1 = timeit.Timer("bubble_sort.bubble_sort_1(x.copy())", "from __main__ import x;import bubble_sort")
# print("bubble_sort:", sort_1.timeit(number=1), "seconds")  # 18-40 seconds
# sort_2 = timeit.Timer("selection_sort.selection_sort(x.copy())", "from __main__ import x;import selection_sort")
# print("selection_sort:", sort_2.timeit(number=1), "seconds")  # 16-40seconds
# sort_3 = timeit.Timer("insertion_sort.insertion_sort(x.copy())", "from __main__ import x;import insertion_sort")
# print("insertion_sort:", sort_3.timeit(number=1), "seconds")  # 14-20seconds
# sort_4 = timeit.Timer("shell_sort.shell_sort(x.copy())", "from __main__ import x;import shell_sort")
# print("shell_sort:", sort_4.timeit(number=1), "seconds")  # 6seconds
sort_5 = timeit.Timer("quick_sort.quick_sort(x.copy(),0,len(x)-1)", "from __main__ import x;import quick_sort")
print("quick_sort:", sort_5.timeit(number=1), "seconds")  # 0.04seconds，太优秀了！
sort_6 = timeit.Timer("merge_sort.merge_sort(list(x.copy()))", "from __main__ import x;import merge_sort")
print("merge_sort:", sort_6.timeit(number=1), "seconds")  # 0.05seconds
sort_7 = timeit.Timer("heap_sort.heap_sort(list(x.copy()))", "from __main__ import x;import heap_sort")
print("heap_sort:", sort_7.timeit(number=1), "seconds")  # 0.05seconds
