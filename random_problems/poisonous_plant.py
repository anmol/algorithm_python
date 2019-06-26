"""poisonous plant hackerrank"""


def poisonousPlants(p):
    n = len(p)
    plant_status = [1] * n
    days = 0
    while True:
        flag = False
        prev = p[0]
        for i in range(1, n):
            if plant_status[i] == 1:
                if p[i] > prev:
                    plant_status[i] = 0
                    prev = p[i]
                    flag = True
        if flag:
            days += 1
        else:
            return days


if __name__ == '__main__':
    ip = [4, 3, 7, 5, 6, 4, 2]
    print poisonousPlants(ip)
