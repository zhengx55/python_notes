import time


def book(name):
    return f"the name of my book is {name}"


def p_decorate(func):
    def wrapper(name):
        return f"<p>{func(name)}</p>"
    return wrapper

# 装饰器包装一个函数之后 即可改变其行为


@p_decorate
def book_dec(name):
    return f"the name of my book is {name}"


def timing_func(func):
    def wrapper():
        start = time.time()
        func()
        stop = time.time()
        return (stop - start)
    return wrapper


@timing_func
def test_list_append():
    lst = []
    for i in range(0, 100000):
        lst.append(i)


@timing_func
def test_list_compre():
    [i for i in range(0, 100000)]


if __name__ == "__main__":
    a = test_list_append()
    c = test_list_compre()
    print("test list append time:", a)
    print("test list comprehension time:", c)
    print("append/compre:", round(a/c, 3))
