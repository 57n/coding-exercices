class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 快慢指針法，slow指針專門指向非0元素放置的位置；fast指針專門遍歷所有元素，發現非0元素時就放到slow的位置
        # 我們會把fast指針指到的非 0 元素和原本在 slow 位置的元素做交換，其他不管，這樣 0 很自然而然就被換到最後面了

        slow = 0
        for fast in range(0, len(nums)):
            if nums[fast] != 0:
                # 因為我們還是要保留 nums[slow]的元素不能覆蓋，所以交換
                nums[fast], nums[slow] = nums[slow], nums[fast] # nums[slow] 如果是0的話，就會透過交換移到後面去了
                slow += 1

class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 另一種更直觀做法，直接把fast指針所指到的非 0 元素取代 slow 指針所在位置的元素，最後再補 0 即可
        slow = 0
        for fast in range(0, len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast] # 直接取代
                slow += 1

        while slow < len(nums):
            nums[slow] = 0 # 最後面再補上0
            slow += 1
            