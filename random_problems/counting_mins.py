"""
count mins between the string having a
time interval
"""


def count_mins(s):
    # split two times
    t1_raw = s.split('-')[0]
    t2_raw = s.split('-')[1]
    t1_12 = get_time_tuple(t1_raw)
    t2_12 = get_time_tuple(t2_raw)
    t1 = convert24(t1_12)
    t2 = convert24(t2_12)

    # if t2[0] >= t1[0] and t2[1] >= t1[1]:
    if t2[0] >= t1[0]:
        mins = (t2[1] - t1[1])
        hr_mins = (t2[0] - t1[0]) * 60
        total = mins + hr_mins
    # elif t2[0] < t1[0]:
    else:
        mins = (t2[1] - t1[1])
        hr_mins = (24 + t2[0] - t1[0]) * 60
        total = mins + hr_mins
    return total


def get_time_tuple(t):
    period = t[-2:]
    hr = t[:-2].split(':')[0]
    min = t[:-2].split(':')[1]
    return hr, min, period


def convert24(t):

    # Checking if last two elements of time
    # is AM and first two elements are 12
    if t[2] == "am" and t[0] == "12":
        return 0, int(t[1])

        # remove the am
    elif t[2] == "am":
        return int(t[0]), int(t[1])

        # Checking if last two elements of time
    # is PM and first two elements are 12
    elif t[2] == "pm" and t[0] == "12":
        return int(t[0]), int(t[1])

    else:

        # add 12 to hours and remove PM
        return int(t[0]) + 12,  int(t[1])


if __name__ == '__main__':
    ti_1 = '9:00am-10:00am'
    ti_2 = '1:00pm-11:00am'
    ti_3 = '1:12pm-11:06am'
    ti_4 = '9:12am-10:06am'
    print count_mins(ti_1)
    print count_mins(ti_2)
    print count_mins(ti_3)
    print count_mins(ti_4)
    # print convert24(('9', '00', 'pm'))
    # print convert24(('9', '00', 'am'))
    # print convert24(('12', '00', 'pm'))
    # print convert24(('12', '00', 'am'))
