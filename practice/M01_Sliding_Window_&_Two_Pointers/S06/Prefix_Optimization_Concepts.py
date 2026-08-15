'''
input nums = [1,2,3,4]
output nums = [1,3,6,10]

nums = [1,2,3,4]
res = [0]*nums
for i in range(len(nums)):
    s=0
    for j in range(i+1):
        s += nums[j]
    nums[i] = s
print(nums)
'''

#1480. Running Sum of 1d Array
from typing import List
def runningSum(nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):

            nums[i]= nums[i]+ nums[i-1]
        return nums
nums = [1,2,3,4]
print(runningSum(nums))

#1732. Find the Highest Altitude

def largestAltitude(gain: List[int]) -> int:
        '''
        n = len(gain)
        alt=[0]* (n+1)
        for i in range(1,n+1):
            alt[i]=alt[i-1]+gain[i-1]
        return max(alt)
        '''

        curr_alt = 0
        max_alt = 0
        for g in gain:
            curr_alt += g
            max_alt = max(curr_alt,max_alt)
        return max_alt
gain = [-5,1,5,0,-7]
print(largestAltitude(gain))

'''
724
523
848
'''

#1991. Find the Middle Index in Array

def findMiddleIndex(nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i 
            left_sum += nums[i]
        return -1
nums = [2,3,-1,8,4]
print(findMiddleIndex(nums))