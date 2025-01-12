class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            # array旋轉後會有兩個半邊至少其中一邊是有序的 
            # 例如 [4,5,6,7,0,1,2]
            # 隨便切一刀，變成左半邊[4,5,6]，右半邊[7,0,1,2]
            # 可以發現左半邊是有序的，從小排到大，右半邊無序的
            # 又例如，左半邊[4,5,6,7,0]，右半邊[1,2]
            # 可以看到左半邊是無序的，右半邊才是有序的，因為從小排到大
            # 只有有序的array才能做binary search，所以我們只要找到有序的array，就可以對它做binary search
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid # 找到了
            
            if nums[left] <= nums[mid]: # 這代表左半邊一定是有序的，左半邊從小排到大，例如左半邊[4,5,6]，mid[7]，右半邊[8,0,1,2]
                # 檢查target是否在左半邊
                if nums[left] <= target < nums[mid]:
                    right = mid - 1 # 代表target就在左半邊，繼續當成正常binary search搜尋，所以right要變成 mid - 1
                else: # 代表target不在左半邊，可惜了，所以target會在右半邊
                    left = mid + 1 # 要去右半邊尋找    
                    
            else: # 當nums[left] > nums[mid] 這代表右半邊一定是有序的，右半邊從小排到大，例如左半邊[4,5,6,7,1]，mid[2]，右半邊[3,4]
                # 檢查target是否在右半邊
                if nums[mid] < target <= nums[right]:
                    left = mid + 1 # 代表target就在右半邊，繼續當成正常binary search搜尋，所以left變成 mid + 1
                else:
                    # 代表target不在右半邊，可惜了，所以target會在左半邊
                    right = mid - 1
        # 找不到
        return -1
        