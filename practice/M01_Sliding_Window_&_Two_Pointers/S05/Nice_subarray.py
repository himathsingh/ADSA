#1248. Count Number of Nice Subarrays
from typing import List
def numberOfSubarrays(nums: List[int], k: int) -> int:
        def sub_arr(k):
            if k < 0:
                return 0
            l,odd,c = 0,0,0
            for r in range(len(nums)):
                if nums[r]%2==1:
                    odd+=1
                while odd > k:
                    if nums[l]%2==1:
                        odd-=1
                    l+=1
                c+=(r-l+1)
            return c
        return sub_arr(k) - sub_arr(k-1)
nums = [1,1,2,1,1]
k = 3
print(numberOfSubarrays(nums,k))


#1763. Longest Nice Substring

def longestNiceSubstring(s: str) -> str:
        if len(s) < 2:
            return ""
        uniq = set(s)
        for i,ch in enumerate(s):
            if ch.lower() in uniq and ch.upper() in uniq:
                continue
            left_str = longestNiceSubstring(s[:i])                     
            right_str = longestNiceSubstring(s[i+1:])   
            return left_str if len(left_str) >= len(right_str) else right_str
        return s                  

s = "YazaAay"
print(longestNiceSubstring(s))