import heapq
from collections import Counter



def stone_weight(stones):
    heap = [ -s for s in stones]
    heapq.heapify(heap)
    while len(heap)>1:
        largest_stone = heapq.heappop(heap)
        second_largest = heapq.heappop(heap)

        if second_largest > largest_stone:
            heapq.heappush(heap, largest_stone - second_largest)
    heap.append(0)
    return abs(heap[0])

def lastStoneWeight( stones):
        heapq._heapify_max(stones)
        while len(stones) > 1:
            max_stone = heapq._heappop_max(stones)
            diff = max_stone - stones[0]
            if diff:
                heapq._heapreplace_max(stones, diff)
            else:
                heapq._heappop_max(stones)

        stones.append(0)
        return stones[0]
if __name__ == "__main__":
    print(stone_weight( [2,7,4,1,8,1]))
    print(lastStoneWeight([2,7,4,1,8,1]))

