def solution(bridge_length, weight, truck_weights):
    time = 1
    brigde_weight = 0
    bridge = []
    for i in range(0, bridge_length):
        bridge.append(0)


    while True:
        brigde_weight -= bridge.pop(0)

        truck = 0
        if len(truck_weights) is not 0:
            truck = truck_weights[0]

        if brigde_weight + truck  > weight:
            bridge.append(0)
        else:
            if len(truck_weights) is not 0:
                truck_weights.pop(0)
            bridge.append(truck)
            brigde_weight += truck

        if brigde_weight <= 0:
            break;

        time += 1

    return time


def main():
    testcases = [
        [2, 10, [7,4,5,6], 8],
        [100, 100, [10], 101],
        [100, 100, [10,10,10,10,10,10,10,10,10,10], 110]
    ]
    
    num = 1
    for tc in testcases:
        print("* %d." % num)
        if solution(tc[0], tc[1], tc[2]) == tc[3]:
            print("  - success")
        else:
            print("  - fail")
        num += 1


if __name__ == "__main__":
    main()
