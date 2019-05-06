class Solution:
	import collections
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_count = collections.Counter(nums)
        
        for i,x in enumerate(nums):
            potential_num = target - x

            if x== potential_num:
                if num_count[potential_num]>1:
                    return [i, nums.index(potential_num, i+1)]
                
            elif potential_num in num_count:
                    return [i, nums.index(potential_num)]
        
        
        