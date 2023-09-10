# 引入多个对象
from math import pow, e, pi

import math as mh
mh.pow(2, 3)

# del 解除名称和对象之间的引用关系

my_name = 'a'
del my_name
# my_name

lang = ['java', 'python', 'php']
del lang[0]
lang = ['java', 'python', 'php']
del lang[:2]
print(lang)

dct = {'name': 'a', 'lang': 'node'}
del dct['lang']
print(dct)
