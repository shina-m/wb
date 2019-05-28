#recursion
class Solution:
    
    def r(self, index, min_index):
        if index > self.l-1:
            return 0

        if self.p[min_index] > self.p[index]:
            min_index = index
      
        gain = self.p[index] - self.p[min_index]

        return max(gain, self.r(index+1, min_index)) 


    def maxProfit(self, prices: List[int]) -> int:
        self.p = prices
        self.l = len(prices)
        return self.r(0, 0)