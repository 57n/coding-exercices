class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 使用「雙指針法」來進行原地去重，時間複雜度 O(n)，空間複雜度 O(1)
        # slow 指針負責標記放置「不重複元素」的位置，fast 指針遍歷整個數組

        slow = 0 # 慢指針從 0 開始，標記唯一元素的插入位置
        for fast in range(1, len(nums)): # 快指針從 1 開始，逐個遍歷數組
            # 碰到 nums[slow] == nums[fast]的情況，fast就是繼續走
            # 直到 nums[slow] != nums[fast]
            if nums[slow] != nums[fast]:
                # 如果找到新的非重複元素，將其放置在 slow+1 的位置
                slow += 1 # slow 位置往前推移，為新元素騰出位置
                nums[slow] = nums[fast] # 將新元素存入 slow 位置

        return slow + 1 # 最後return有幾個不重複的數字 (索引從 0 開始，因此回傳 slow + 1)