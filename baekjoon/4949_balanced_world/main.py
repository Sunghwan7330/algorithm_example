from collections import deque

RET_YES = "yes"
RET_NO = "no"

def isBalanced(str):
    stack = deque()

    for c in str:
        #print(c)
        if c == '[' or c == '(':
            stack.append(c)
        elif c == ']':
            if len(stack) == 0:
                return RET_NO
            d = stack.pop()
            if d != '[':
                return RET_NO
        elif c == ')':
            if len(stack) == 0:
                return RET_NO
            d = stack.pop()
            if d != '(':
                return RET_NO
    
    if len(stack) != 0:
        return RET_NO
        
    return RET_YES


def solution():
    while True:
        str = input()
        if str == '.':
            break
        print(isBalanced(str))

solution()
    
