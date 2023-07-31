def solution(my_string):
    answer = 0
    
    token = my_string.split()
    answer = int(token[0])
    for i in range(1, len(token), 2):
        print(i)
        if token[i] == '+':  answer += int(token[i+1])
        elif token[i] == '-':  answer -= int(token[i+1])

    return answer
