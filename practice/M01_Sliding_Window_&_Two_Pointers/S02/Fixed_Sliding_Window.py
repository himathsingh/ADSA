#643. Maximum Average Subarray I
#brute force
from typing import List
def findMaxAverage(nums: List[int], k: int) -> float:
        max_avg=float("-inf")
        n=len(nums)
        for i in range(0,n-k+1):
            sub_sum=0
            for j in range(i,k+i):
                sub_sum += nums[j]
            max_avg = max(max_avg,sub_sum/k)
        return max_avg
nums=[1,12,-5,-6,50,3]
k=4
print(findMaxAverage(nums,k))

def findMaxAverage_optimal(nums: List[int], k: int) -> float:
    n=len(nums)
    win_sum=sum(nums[0:k])
    for i in range(n-k):
        next_win_sum=win_sum-nums[i]+nums[i+k]
        win_sum=max(win_sum,next_win_sum)
    return win_sum/k
nums=[1,12,-5,-6,50,3]
k=4
print(findMaxAverage_optimal(nums,k))

#1343Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    win_sum = sum(arr[0:k])
    c = 0
    n = len(arr)
    if(win_sum/k)>= threshold:
        c +=1
    for i in range(n-k):
        win_sum = win_sum - arr[i]+ arr[k+i]
        if (win_sum/k)>= threshold:
            c +=1
    return c
arr = [11,13,17,23,29,31,7,5,2,3]
k = 3
threshold = 5
print(numOfSubarrays(arr,k,threshold))

