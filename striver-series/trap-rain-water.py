from typing import List


def trap(height: List[int]) -> int:
    start = height[0]
    i = 0
    trapped_water = 0
    prefix_sum = []
    prefix_sum.append(height[0])
    suffix_sum = [0]*len(height)

    suffix_sum[len(height)-1] = height[len(height)-1]
    for i in range(1,len(height)):
        prefix_sum.append(max(prefix_sum[i-1],height[i]))

    for j in range(len(height)-2,0,-1):
        suffix_sum.append(max(suffix_sum[j+1],height[j]))
    w = 0
    for i in range(len(height)):
        w +=min(prefix_sum[i], suffix_sum[i]-height[i])
    print(prefix_sum,suffix_sum)
    print(w)

    # while i<len(height):
    #     print("i is", i,trapped_water)
    #     if start < height[i+1]:
    #         start = height[i]
    #         i+=1
    #     else:
    #         start = height[i]
    #         for j in range(i+1,len(height)):
    #             if height[j]>=start:
    #                 i,start = height[j],j
    #                 break
    #             else:
    #                 trapped_water += start - height[j]
    #         else:
    #             i+=1

    return trapped_water

if __name__=="__main__":
    trap( [0,1,0,2,1,0,1,3,2,1,2,1])