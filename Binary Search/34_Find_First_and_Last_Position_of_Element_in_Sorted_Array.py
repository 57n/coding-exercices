class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 思路：要找 first 和 last position，就是要找最後邊界以及最左邊界。可以套用binary search找最右以及最左邊界的模板
        # 總共做兩次binary search

        # 找最左邊界
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target: # nums[mid] < target代表mid應該要往右移，直到 nums[left] 等於 target為止
                left = mid + 1
            else:
                # nums[mid] > target代表mid應該要往左移
                # nums[mid] == target時，mid也還是要往左移，因為我們要找的是最左邊界
                right = mid - 1
        # 最後最左邊界會停留在left的位置，因為最後一次迴圈時left會==right，或是left和right只差1，如果nums[mid] < target
        # 此時 left = mid + 1，nums[left]理應就要等於target，left位置就會是最左邊界
        # 若nums[mid] >= target(此時nums[mid]應該是要等於target的)，也代表left早已在最左邊界。
        first = left
        # 需要注意的是找不到的情況，例如1,2,3,4,6，要找5，此時left會停留在6的位置。
        # 或是7,8,9,10，要找6，此時left會停留在0的位置
        # 或是6,7,8，要找9，此時left會超出邊界
        if left == len(nums) or nums[left] > target:
            return [-1, -1] # 其實這時候就沒必要找右邊界了...

        # 找最右邊界
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                # nums[mid] < target代表mid應該要往右移
                # 當 nums[mid] == target時，mid還是要往右移，因為我們要找最右邊界
                left = mid + 1
            else:
                right = mid - 1 # nums[mid] > target時，代表nums[mid]太大，整個 mid 要往左移
        
        # 迴圈最後一步時，left會==right，或是left和right會差1，如果nums[mid] 還是> target，這時候mid-1就應該等於target了，而mid-1就是right
        # right 所處位置就會是最右邊界
        last = right
        # 需要注意的是找不到的情況，例如1,2,3,4,6，要找5，此時right會停留在4的位置。
        # 或是7,8,9,10，要找6，此時right會停留在-1的位置(超出邊界)
        # 或是6,7,8，要找9，此時right會停留在len(nums)-1的位置
        if right < 0 or nums[right] < target:
            last = -1

        if first == -1 or last == -1:
            return [-1, -1]
        
        return [first, last]
        
            