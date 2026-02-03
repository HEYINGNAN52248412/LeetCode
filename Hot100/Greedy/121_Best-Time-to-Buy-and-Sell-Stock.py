#the nested loop traversed with every possible buying days.abs
#but we dont need to do that. just maintain a "current cheapest day"
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            lowest = min(lowest, prices[i])
            if prices[i] > lowest:
                max_profit = max(max_profit, prices[i] - lowest) 

        return max_profit
                