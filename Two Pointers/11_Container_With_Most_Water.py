class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        解法：雙指針法（Two Pointers Approach）
        1.	為什麼要從兩邊開始？
        •	兩邊的距離最遠，能夠獲得較大的水量範圍。
        •	逐步縮小範圍，尋找更高的柱子來增加容量。
        2.	為什麼要移動較短的一側？
        •	水量受限於較短的那一邊，若保持不變則無法增加容積，因此嘗試找到更高的柱子。

        時間複雜度：O(n) -> 每次移動指針，逐漸縮小問題範圍。
        空間複雜度：O(1) -> 只使用常數級變數。
        '''

        # 從兩邊開始
        left = 0
        right = len(height) - 1

        max_area = 0
        while left < right:
            # 計算當前區間的水量，受限於較短的柱子
            area = min(height[right], height[left]) * (right - left)
            if area > max_area:
                max_area = area
            if height[right] < height[left]:
                right -= 1 # 移動較短的一側，因為水量取決於較短的那根柱子
            else:
                # 相同時，可以動right，也可以動left，這裡就動left
                # height[left] 比 height[right]短，所以儘可能移動left，保留right的位置，說不定下一個left比較長
                left += 1
        return max_area