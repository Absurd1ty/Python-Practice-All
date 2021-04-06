"""You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes."""

class Solution:
    def minOperations(self, boxes: str):
        total_moves = [0]*len(boxes)
        left_count = 0
        left_steps = 0
        right_count = 0
        right_steps = 0
        size = len(boxes)
        for i in range (1, size):
            if boxes[i-1] == '1':
                left_count += 1 
            left_steps += left_count
            total_moves[i] = left_steps
        for i in range(size-2, -1, -1):
            if boxes[i+1] == '1':
                right_count += 1
            right_steps += right_count
            total_moves[i] += right_steps
        return total_moves
"""Runtime: 64 ms, faster than 95.56% of Python3 online submissions for Minimum Number of Operations to Move All Balls to Each Box.
Memory Usage: 14.5 MB, less than 93.27% of Python3 online submissions for Minimum Number of Operations to Move All Balls to Each Box."""

    result = Solution().minOperations("001011")
print(result)