class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 解題思路：把二維陣列看成一維陣列來做binary search，但需要找到一維二維間的轉換公式，就可以套用binary search的模板
        row_num = len(matrix)
        col_num = len(matrix[0])
        left = 0
        right = row_num * col_num - 1

        while left <= right:
            mid = (left + right) // 2

            # 一維轉成二維的公式
            row = mid // col_num
            col = mid % col_num

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1 # mid要往右移
            else:
                right = mid - 1
        return False