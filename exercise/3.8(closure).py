'''
3.8 题目
g(0)+g(1) => 0
g(1)+g(0) => 1
'''


def f():
    num = 1

    def calc(a):
        nonlocal num
        if a == 0:
            num = 0
            return num
        else:
            num = num*(num+1)//2
            return num
    return calc


g = f()
# print(g(1))
# print(g(0))
print(g(0))
print(g(1))
