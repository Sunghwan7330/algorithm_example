def get_count(a, b):
    if b == 0:
        return a
    if b == 3:
        return a + 1

    while a > 0:
        a -= 1
        b += 5
        q, r = divmod(b, 3)
        if r == 0:
            return a + q 
    
    return -1

def solution():
    n = int(input())
    a, b = divmod(n, 5)
    print(get_count(a, b))

    return

solution()