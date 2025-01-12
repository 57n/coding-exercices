class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # 思路：matrix會出現在matrix[0][0]，最大值會出現在matrix[n-1][n-1]
        # 可以做binary search，給定一個值mid，我們就算出mid在矩陣中有多少數小於等於k
        # 最終的目標是讓 left 和 right 收斂到第 k 小的數值
        
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n-1][n-1]

        def count_ranking(mid):
            # 計算mid是矩陣中第幾小
            count = 0
            # 我們選擇從左下角開始搜尋
            '''
        1. 左下角
        •	特性：
        •	行升序，向上元素更小。
        •	列升序，向右元素更大。
        •	搜索策略：
        •	如果當前值 matrix[row][col] <= mid，那麼 整列上方的元素也都小於等於 mid，可以將指針向右移動（col++）。
        •	如果當前值 matrix[row][col] > mid，說明當前行有較大的值，向上移動（row--）。
        •	為什麼適合？
        •	容易判斷移動方向，且能涵蓋整個矩陣。
        2. 右上角
        •	特性：
        •	行升序，向下元素更大。
        •	列升序，向左元素更小。
        •	搜索策略：
        •	如果當前值 matrix[row][col] <= mid，那麼 整行左側的元素也都小於等於 mid，可以將指針向下移動（row++）。
        •	如果當前值 martix[row][col]} > mid，說明當前列有較大的值，向左移動（col--）。
        •	為什麼適合？
        •	同樣具有清晰的移動方向，且從右上角開始能快速涵蓋範圍。
        3. 左上角
        •	特性：
        •	行升序，向下元素更大。
        •	列升序，向右元素更大。
        •	問題：
        •	如果從左上角開始：
        •	當前值小於等於 mid 時，既可以向右移動也可以向下移動，無法唯一確定下一步方向。
        •	這會導致搜索邏輯變得混亂，難以實現高效統計。
        4. 右下角
        •	特性：
        •	行升序，向上元素更小。
        •	列升序，向左元素更小。
        •	問題：
        •	如果從右下角開始：
        •	當前值大於 mid 時，既可以向上移動也可以向左移動，無法唯一確定下一步方向。
        •	搜索方向模糊，會導致不必要的重複計算。
            '''
            col = 0
            row = n-1
            # 從左下角開始，每次往右一步或往上一步走，每步走完後，計算所在位置以及直排上方有多少元素 <= mid，並加總
            while col < n and row >= 0:
                if mid >= matrix[row][col]:
                    count += row + 1 # 當 mid 大於等於 matrix[row][col] 時，matrix[row][col] 及其以上的元素一定小於等於 mid
                    col += 1 # 移動到下一的col去比較
                else:
                    # 代表此時 mid 所在位置 matrix[col][row] 比 mid 大，只好往上一排去看看
                    row -= 1
            return count
                
                    
                    

        while left < right: # 收斂條件：二分搜尋會逐步縮小 [left, right] 的範圍，最終 left 和 right 收斂到第 k 小的數。，故不能用left <= right
            mid = (left+right) // 2
            # 寫個函數count_ranking計算矩陣中有多少個數 <= mid，例如當k=3，我們要找到一個mid使得count_ranking(mid)==3
            '''
            請注意，當 count_ranking(mid) == k，不代表已經找到了
            例如 1,3,5,7,9,11。 k = 3，第三小的數是5，此時你用mid = 6代入，count_ranking(mid) 會算出有3個數小於等於6
            這時候我們仍然要把mid變小向左移，希望能找到5，所以請注意當等於的情況時是向左移
            '''
            if count_ranking(mid) < k: 
                left = mid + 1 # 代表mid太小了，需要向右移
            else:
                # 如果排名很後面，代表數值很大，向左移
                # 需要注意的是，當count_ranking(mid) == k等於時也要向左移，但因為mid可能就是我們要找的值，所以right = mid，而不是 right = mid - 1
                right = mid 

        return left
        