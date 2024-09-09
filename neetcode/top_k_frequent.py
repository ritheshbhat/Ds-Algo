import heapq
from collections import Counter


def k_elem(arr,kk):
    c = Counter(arr)
    heap = []
    for k,v in c.items():
        heapq.heappush(heap, (-v,k)) #max heap

    for _ in range(kk):
        print(heapq.heappop(heap)[1])


s = ""
k_elem([1,1,2,3,4,5,5,5], 2)