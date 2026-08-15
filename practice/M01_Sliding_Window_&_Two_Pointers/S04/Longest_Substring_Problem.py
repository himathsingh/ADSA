#3. Longest Substring Without Repeating Characters

def lengthOfLongestSubstring(s: str) -> int:
        s1 = set()
        left =  0
        max_len = 0
        for right in range(len(s)):
            while s[right] in s1:
                s1.remove(s[left])
                left +=1
            s1.add(s[right])
            max_len = max(max_len,right - left +1)
        return max_len
s = "pwwkew"
print(lengthOfLongestSubstring(s))

#1493. Longest Subarray of 1's After Deleting One Element

from typing import List
def longestSubarray(nums: List[int]) -> int:
        l = 0
        z = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                z +=1
            while z > 1:
                if nums[l] ==0:
                    z -=1
                l +=1
            max_len = max(max_len,right - l + 1)
        return max_len-1
nums = [1,1,0,1]
print(longestSubarray(nums))

#1004. Max Consecutive Ones III