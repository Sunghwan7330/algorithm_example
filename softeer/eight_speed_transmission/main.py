import sys

def checkAsecnding(gear_num):
    for i in range(len(gear_num)):
        if i+1 != gear_num[i]:
            print("mixed")
            return
    
    print("ascending")
    return

def checkDescnding(gear_num):
    for i in range(len(gear_num)):
        if 8-i != gear_num[i]:
            print("mixed")
            return
    
    print("descending")
    return

def solution(gear_num):
    
    if (gear_num[0] == 1): 
        checkAsecnding(gear_num)
    elif (gear_num[0] == 8): 
        checkDescnding(gear_num)
    else:
        print("mixed")
        return

    return

def main():
    input_arr = list(map(int, input().split()))
    #print(input_arr)
    solution(input_arr)
    return


main()