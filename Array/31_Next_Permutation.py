class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        解法：三步翻轉法 (找-換-翻)
        """
        
        # 1. 找：從右往左找到第一個下降的元素（pivot）。因為從左到右都沒有下降的區間的話會發現不會有下一個permutation
        # 以 [1,3,5,4,2] 為例：
        # 找到第一個下降的數字：3，因為 3 < 5。
        '''
        [1, 3, 5, 4, 2]
            ^
        '''

        # 2. 換：從右往左找到第一個比 pivot 大的元素，交換它們，使字典序變大
        # 在右邊找到比 3 大的最小數字：4，交換它們。
        '''
        [1, 4, 5, 3, 2]
        '''

        # 3.翻：反轉 pivot 右邊的元素，使其變成最小排列。
        # 反轉 5,3,2 使其變成最小排列：
        '''
        [1, 4, 2, 3, 5]
        '''

        # 從右往左找到第一個下降的元素的index i
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        # 注意：若找不到 pivot（完全遞減排列，如 [5,4,3,2,1]），i 會變成 -1

        # 從右往左找到第一個比 nums[i] 大的元素，交換它們。
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # 反轉 pivot 右邊的元素，使其變成最小排列。
        left = i + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1