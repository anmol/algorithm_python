import heapq

#
# Complete the runningMedian function below.
#


def running_median(a, n):
    #
    # Write your code here.
    #
    min_heap = []
    max_heap = []
    out = []
    median = 0
    for i in range(n):
        if a[i] > median:
            heapq.heappush(min_heap, a[i])
        else:
            heapq.heappush(max_heap, -a[i])
        if abs(len(min_heap) - len(max_heap)) > 1:
            if len(min_heap) > len(max_heap):
                item = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -item)
            else:
                item = -heapq.heappop(max_heap)
                heapq.heappush(min_heap, item)
        if abs(len(min_heap) - len(max_heap)) == 0:
            median = float(min_heap[0] +(-max_heap[0]))/2
        elif len(min_heap) > len(max_heap):
            median = float(min_heap[0])
        else:
            median = float(-max_heap[0])
        out.append(median)
    return out


if __name__ == '__main__':
    ip = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(running_median(ip, len(ip)))
