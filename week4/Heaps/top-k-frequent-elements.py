class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        
        c = collections.Counter(nums)
        r = heapq.nlargest(k, list(c.keys()), key = lambda x: c[x]) 
        return r