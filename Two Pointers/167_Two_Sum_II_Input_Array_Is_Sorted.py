class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # # 題目要求只能使用 O(1) 額外空間，不能使用 Hash Map，否則空間複雜度會是 O(n)
        # 因為 numbers 是已排序（sorted）的，適合用雙指針（Two Pointers）解法，時間複雜度是 O(n)
        
        # 初始化兩個指針：left 從開頭，right 從尾端
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right +1] # 題目要求回傳 1-based index，所以要加 1
            if numbers[left] + numbers[right] > target:
                # 總和太大，右指針往左移動以減少總和（因為數列已排序）
                right -= 1
            else:
                # 總和太小，左指針往右移動以增加總和（因為數列已排序）
                left += 1