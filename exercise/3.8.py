'''
3.8 题目
f(0)+f(1) => 0
f(1)+f(0) => 1
'''
global num
num = 1


def f(a):
    global num
    if a == 0:
        num = 0
        return num
    else:
        num = num*(num+1)//2
        return num


# print(f(1))
# print(f(0))
print(f(0))
print(f(1))
