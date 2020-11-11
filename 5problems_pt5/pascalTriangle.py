"""Given a non-negative integer numRows, generate the first numRows of Pascal's triangle"""
class Solution(object):
    def generate(self, numRows):
        pascal_triangle = []
        for row in range(1, numRows+1):
            new_row = [1]*row
            for place in range(1, row-1):
                new_row[place]=pascal_triangle[-1][place-1] + pascal_triangle[-1][place] 
            pascal_triangle.append(new_row)
        return pascal_triangle

result = Solution().generate(10)
print(result)