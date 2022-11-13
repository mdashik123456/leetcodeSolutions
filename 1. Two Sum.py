class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for indx, val in enumerate(nums):
            sub = target - val
            if sub in hashMap:
                return [hashMap[sub], indx]
            else:
                hashMap[val] = indx
