import sys

def solution(k, p, n):
    res = 1
    mod_val = 1000000007
    for i in range(n):
        res = (res * p) % mod_val

    return (res * k) % mod_val

def main():
    arr = list(map(int, input().split()))
    print(solution(arr[0], arr[1], arr[2]))
    return

main()