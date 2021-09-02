def convert_int_to_time(time_int):
    hour = time_int // 3600
    time_int = time_int % 3600
    min = time_int // 60
    time_int = time_int % 60
    sec = time_int
    return "%02d:%02d:%02d" % (hour, min, sec)

def convert_time_to_int(time):
    time_arr = time.split(':')
    hour = int(time_arr[0])
    min = int(time_arr[1])
    sec = int(time_arr[2])
    return (hour * 3600) + (min * 60) + sec

def solution(play_time, adv_time, logs):
    play_time_int = convert_time_to_int(play_time)
    adv_time_int = convert_time_to_int(adv_time)

    total_time = [0 for i in range(play_time_int+1)]

    for log in logs:
        log_arr = log.split('-')
        start_time = convert_time_to_int(log_arr[0])
        end_time = convert_time_to_int(log_arr[1])
        """
        diff = end_time - start_time
        for i in range(diff):
            total_time[start_time + i] += 1
        """
        total_time[start_time] += 1
        total_time[end_time] -= 1
    for i in range(play_time_int-1):
        total_time[i+1] = total_time[i+1] + total_time[i]

    temp_sum = 0

    for i in range(adv_time_int):
        temp_sum += total_time[i]

    max_watch = temp_sum
    max_time = 0

    for i in range(play_time_int - adv_time_int):
        temp_sum -= total_time[i]
        temp_sum += total_time[i + adv_time_int]
        if(temp_sum > max_watch):
            max_watch = temp_sum
            max_time = i + 1
    """ # FOR DEBUG
    for i in range(play_time_int):
        print(convert_int_to_time(i) + " - " + str(total_time[i]))
    """
    #print(convert_int_to_time(max_time))

    return convert_int_to_time(max_time)


def main():
    testcases = [
       ["02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"], "01:30:59"],
       ["99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"], "01:00:00"],
       ["50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"], "00:00:00"]
    ]

    num = 1
    print("* %d." % num)
    for tc in testcases:
        ret = solution(tc[0], tc[1], tc[2])
        if ret == tc[3]:
            print("  - success")
        else:
            print("  - fail")
        num += 1

if __name__ == '__main__':
    main()