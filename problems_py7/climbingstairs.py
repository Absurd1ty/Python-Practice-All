"""On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps. You need to find minimum cost 
to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1."""

class Solution:
    def minCostClimbingStairs(self, cost: [int]):
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 2], cost[i - 1])
            print (cost[i])
        return min(cost[-1], cost[-2])

result= Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
print(result)