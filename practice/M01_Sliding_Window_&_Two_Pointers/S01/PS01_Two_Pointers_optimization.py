#26. Remove Duplicates from Sorted Array
from typing import List
def removeDuplicates(nums: List[int]) -> int:
        i =0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))

#27. Remove Element
def removeElement(nums: List[int], val: int) -> int:
        i = 0
        for j in range(0,len(nums)):
            if nums[j]!= val:
                nums[i]=nums[j]
                i+=1
        return i
nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums,val))


#167. Two Sum II - Input Array Is Sorted

def twoSum(numbers: List[int], target: int) -> List[int]:
        left,right = 0,len(numbers)-1
        while left<right:
            s = numbers[left]+numbers[right]

            if s == target:
                return[left+1,right+1]
            elif s> target:
                right -=1
            else:
                left +=1
numbers = [2,7,11,15]
target = 9
print(twoSum(numbers,target))

#977. Squares of a Sorted Array
