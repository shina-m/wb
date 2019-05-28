#dp
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_preceding_price = sys.maxsize
        max_gain = 0
        gain = [0] * len(prices)
        
        for i,x in enumerate(prices):
            min_preceding_price = min(min_preceding_price, x)
            gain[i] = x - min_preceding_price
            max_gain = max(max_gain, gain[i])
            
        return max_gain