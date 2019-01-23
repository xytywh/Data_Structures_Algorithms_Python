class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            result = [[1], [1, 1]]
            temp = []
            for i in range(numRows - 2):
                temp = [1] * (i + 3)
                res = result[-1]
                for j in range(len(res) - 1):
                    temp[j + 1] = res[j] + res[j + 1]
                result.append(temp)
        return result
