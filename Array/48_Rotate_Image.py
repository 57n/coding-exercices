class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        解題思路：先轉置矩陣，再水平翻轉
        1. 轉置矩陣：轉置就是行變列，列變行，做法是矩陣沿對角線（左上至右下）交換
        [1,2,3],                                         [1, 4, 7]
        [4,5,6], ------> 2,4 交換，3,7交換，6,8交換 ------> [2, 5, 8]
        [7,8,9]                                          [3, 6, 9]
        
        2. 接著每一列水平翻轉
        [1, 4, 7]         [7, 4, 1]
        [2, 5, 8] ------> [8, 5, 2]
        [3, 6, 9]         [9, 6, 3]

        時間複雜度: O(n^2) 需要訪問矩陣中的每個元素兩次
        空間複雜度: O(1) 直接在原矩陣進行操作，無需額外空間
        '''

        n = len(matrix[0])
        # 只需要走矩陣一半，沿對角線交換
        # [1, 4, 7]
        #     5, 8]
        #        9]
        for row in range(n):
            for col in range(row, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # 水平翻轉
        for i in range(n):
            left = 0
            right = n - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1