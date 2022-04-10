lst = [i for i in range(2,101,2)]
print(lst)
result = [0, 1]
for i in range(10):
    result.append(result[-2] + result[-1])
print(result)
res = [0, 1]
re = [res[-2] + res[-1] for i in range(10)]
print(re)