
# input: 1,3,5,5,11,8,5,3 
# output: 1, 3,5,8,11


def custom_sort(ip):
    input_array = sorted(ip)
    n = len(input_array)

    l = [input_array[0]]

    for i in range(1, n):
        if input_array[i] != input_array[i-1]:
            l.append(input_array[i])
    return l


def custom_sort2(ip):
    n = len(ip)
    i = 0
    j = n-1
    while i != j:
        if ip[i] < ip[j]:
            print(ip[i])
            i += 1
            while ip[i] == ip[i-1] and i < j:
                i += 1
        elif ip[i] > ip[j]:
            print(ip[j])
            j -= 1
            while ip[j] == ip[j-1] and j > i:
                j -= 1
        else:
            print(ip[i])
            i += 1
            while ip[i] == ip[i-1] and i < j:
                i += 1
            j -= 1
            while ip[j] == ip[j-1] and j > i:
                j -= 1
    print(ip[i])


if __name__ == '__main__':
    ip = [1,3,5,5,11,8,5,3]
    # print(custom_sort(ip))
    custom_sort2(ip)