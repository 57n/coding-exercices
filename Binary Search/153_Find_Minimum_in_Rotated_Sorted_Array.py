class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 這題可以用 33. Search in Rotated Sorted Array的概念做binary search，原本是先找到有序的部分並討論看要搜尋有序還是無序的部分
        # 這題就改成把目標值變成最小值會出現在哪一段做討論

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid]: # 左半邊是有序的 
                if nums[mid] > nums[right]: # 最小值在右半邊 ex. [4, 5, 6, 7, 0, 1, 2]
                    #                                         left     mid
                    left = mid + 1
                else: 
                    # nums[mid] < nums[right]，代表從left ~ right都是有序的 ex. [4,  5,  6,  7]
                    #                                                        left        right
                    # 此時最小值在左半邊
                    # 注意用 mid = right - 1 會出錯，因為 mid 有可能是最小值，需要保留
                    # ex. [ 4,   5]
                    #     left  right
                    #     mid
                    right = mid
                    
            else:
                # nums[left] > nums[mid] 代表
                # 右半邊是有序的 ex. [5, 0, 1, 2, 3, 4]
                #                 left   mid
                # 此時最小值一定在左半邊
                right = mid # 注意這裡不是 mid - 1，因為 mid 有可能是最小值，需要保留
                #  ex. [4, 5, 0, 1, 2, 3]
                #     left   mid
        
        # 我們最後要讓程式收斂在left == right，此時 nums[left] == nums[right]在最小值位置
        # 所以迴圈要設計成 while left < right 而不是 while left <= right
        # 在 while left <= right 的情況下，當 left == right 時，仍然會進行一次迭代，而這通常是沒有必要的。
        # while left < right 的寫法，保證迴圈在剩下一個元素時（left == right）停止，不需要再進行多餘的比較。'

        #為什麼 nums[left] 是最小值
        #•	根據二分邏輯，每次調整範圍時，我們保證了最小值始終在 [left, right] 之間：
        #•	如果 nums[mid] > nums[right]，最小值在右半邊（排除 mid，所以 left = mid + 1）。
        #•	如果 nums[mid] <= nums[right]，最小值在左半邊（可能包含 mid，所以 right = mid）。
        #•	當範圍縮小到一個元素時，nums[left] 或 nums[right] 都指向這個唯一的元素，即最小值。
        return nums[left]