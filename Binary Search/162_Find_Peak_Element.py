class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # 原本不考慮edge case的寫法
            # if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            #      return mid

            # 加上邊界判斷
            # mid == 0 就不用檢查nums[mid] > nums[mid-1]，所以加個 or
            # mid == len(nums) - 1 就不用檢查nums[mid] > nums[mid+1]，所以加個 or
            # 這樣也同時 cover 到 len(nums) == 1 的情況，因為符合 mid == 0 and mid == len(nums)-1的情況
            if (mid == 0 or nums[mid] > nums[mid-1]) and (mid == len(nums)-1 or nums[mid] > nums[mid+1]):
                return mid

            if nums[mid] < nums[mid-1] and mid - 1 >= 0:
                right = mid - 1 # 左邊會有peak，因為 mid - 1，就是左邊的數字更大
            else:
                left = mid + 1 # 右邊會有peak，因為 mid比左邊數字大，所以往右邊找更合理
        
        return -1 