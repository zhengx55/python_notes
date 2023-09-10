'''
    get(key, default=None)
    在get的参数中包含key和一个default
    
'''

'''
    setdefault(key, default=None)
    如果key不在dict中, 则插入值为default的key
'''
d = {"name": "laoqi", "city": ['shanghai', 'soochow', 'hangzhou']}
d.setdefault('name')    # 同 get() 方法
d.setdefault('age')

dct = {"book": "learn python", "price": 99}
print(dct.keys())
print(dct.values())
print(dct.items())
# 以上操作的返回值, 在python中被称为视图对象, 字典一旦发生改变, 其视图对象也会i发生改变

# update()
update_dct = {'book': 'learn python', 'price': 89}
author = {'name': 'abc', 'age': 28}
update_dct.update(author)
print(update_dct.keys())

# author 更新了字典但是并没有生成新的对象

# pop() popitem() clear()
'''
pop()
D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, default is returned if given, otherwise KeyError is raised
'''

'''
popitem()
Remove and return a (key, value) pair as a 2-tuple.

    Pairs are returned in LIFO (last-in, first-out) order.
    Raises KeyError if the dict is empty.
'''
