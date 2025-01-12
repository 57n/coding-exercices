class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # 注意這題當 num[mid] == target 時，mid只有兩個選擇，往左移或不動，往左移是因為要找第一個插入位置，要往左移只能縮小right
            # 當 num[mid] > target時，很明顯就要讓mid往左移，這時需修改right的位置
            if  nums[mid] < target: 
                # 只有當 nums[mid] < target時，才需要讓mid往右移。當nums[mid] == target時，就如上述所說，mid不能往右
                left = mid + 1
            else:
                right = mid - 1 # 當 num[mid] == target 或  num[mid] > target 時，mid需要往左移
        
        # 當nums[mid] == target時，會一直把right往左移，最後right會停在插入位置的右邊一格，所以這時候要return left
        # 也不能return mid，因為最後一次迴圈可能停在這個狀態  if  nums[mid] < target，這樣return mid 很不合理
        return right+1
        