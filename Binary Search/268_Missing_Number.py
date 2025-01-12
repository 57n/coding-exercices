class Solution1(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 原始數列 = [0, 1, 2, 3.... n]
        # 原始加總 = (0 + n) / 2 * (n + 1)
        n = len(nums)
        original_sum = int(n * (n + 1) / 2)
        current_sum = sum(nums) # 目前加總
        return original_sum - current_sum #缺失數 = 原始加總 - 目前加總

class Solution2(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left = 0
        right = len(nums) - 1

        while left <= right: # 注意是 <=，因為在left==right時還是要做最後比對，看是left右移還是right左移
            mid = (left + right) // 2
            if nums[mid] == mid: # 如果nusm[mid] = mid，代表mid之前的數列都沒有缺失，缺失的在mid右邊
                left = mid + 1
            else: # 如果nums[mid] != mid，代表mid之前的數列有缺失，缺失的在mid左邊
                right = mid - 1
        # 目標是找到第一個 nums[mid] != mid，亦即找到最小不符合nums[mid] = mid的最小mid，可以視為找最左邊界問題。   # 此時 left 指向缺失數字的位置
        return left
        
        