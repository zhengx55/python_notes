# 列表解析
import time
[i*i for i in range(1, 10)]

# 检查运行时间

start_time = time.time()
lst = [i*i for i in range(100000)]
end_time = time.time()
delta = end_time - start_time

print(f"list comprehension time:{delta}")

start_time_2 = time.time()
lst2 = []
for i in range(100000):
    lst2.append(i*i)
end_time_2 = time.time()
delta_2 = end_time_2 - start_time_2

print(f"list append time:{delta_2}")

# 例如，选出列表 ['anwang', 'microsoft', 'ibm', 'compaq', 'lenovo', 'dell'] 中含有字母 'a' 的单词：
lst = ['anwang', 'microsoft', 'ibm', 'compaq', 'lenovo', 'dell']

[word for word in lst if 'a' in word]

gender = ['male', 'female']

[0 if gen == 'female' else 1 for gen in gender]

# dict 操作
myinfor = {"publish": "phei", "site": "itdiffer.com", "lang": "python"}

{v: k for k, v in myinfor.items()}

print(myinfor.items())