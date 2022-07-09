# 将a中n个物体移动到c

def haoni(n, a, b, c):
    if n > 0:
        haoni(n-1, a, c, b)
        print(a + ' to ' + c)
        haoni(n-1, b, a, c)


haoni(3, 'a', 'b', 'c')
