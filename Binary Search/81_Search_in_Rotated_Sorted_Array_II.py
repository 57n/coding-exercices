class Solution(object):
    def search(self, nums, target):
        # 解題思路： 這題和 Search in Rotated Sorted Array I 一樣解法，只是 array 會有duplicate items
        # 所以需要處理 nums[left] == nums[mid] == nums[right]的情況
        left = 0
        right = len(nums) - 1
        # 先用不重複的例子去找區間 [4,5,6,7,0,1,2]
        # 再用重複的例子去想edge case [2,5,6,0,0,1,2]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            # Search in Rotated Sorted Array I的思路是，找到有序的區間，對有序的區間做binary search，我們先寫成I的版本，再去思考有重複值的情形
            if nums[left] == nums[mid] == nums[right]: # 請看後面註解
                left += 1
                right -= 1
                # 若始終碰到 nums[left] == nums[mid] == nums[right] 而必須不斷縮邊界，
                # 可能導致最糟 O(n) 的行為，但平均而言仍可達到較佳的效率。
            # 這裡一開始我們先寫成 if nums[left] < nums[mid]，先不討論等於的情形，後續再來討論等於的情形並改成elif nums[left] <= nums[mid]:
            # 因為在沒有重複值混淆時，若 nums[left] == nums[mid]，那就表示整個 [left, mid] 是按升序排列的
            # 當有重複值時且nums[left] == nums[mid]，若沒有同時滿足 nums[left] == nums[right] 等情況，[left, mid] 依然可以視作有序。（這部分請看後面註解說明才能理解）
            elif nums[left] <= nums[mid]: # 代表left ~ mid 之間一定是有序的，就來試著找找看
                # 注意不需要寫成 nums[left] <= target <= nums[mid]，會進到這裡就代表 target != nums[mid] 了！
                if nums[left] <= target < nums[mid]: # target 在 left ~ mid 之間，可以繼續對這區間做binary search
                    right = mid - 1
                else: # target 不在 left ~ mid這區間，換個區間唄，因此將搜尋範圍改為 [mid+1, right]
                    left = mid + 1
            elif nums[left] > nums[mid]: 
                # 代表left ~ mid 不是有序的，此時 mid ~ right區間一定是有序的
                if nums[mid] < target <= nums[right]: # target 在 mid ~ right 之間，可以繼續對這區間做binary search
                    left = mid + 1
                else: # target 不在 mid ~ right 這區間，換個區間試試唄，因此將搜尋範圍改為 [left, mid-1]
                    right = mid - 1

            # 討論 nums[left] == nums[mid]的狀況
            # 1. left == mid，可以視為有序
            # 2. nums[left] ~ nums[mid]之間都是一樣的，可以視為有序
            # 3. [x, x-2, x-1,  x, ....]     [x, x+1, x+2, x, ...]  這狀況無法判定
            #    left          mid           left         mid
            # 發現條件1很好寫，發現條件2必須要用O(n)的方式才能判斷，不好寫，因為會有[x, x, x+1, x, x...]的情況
            #                                                           left           mid 
            # 觀察條件三可以發現無法判定的情形此時nums[left] == nums[mid]外還會等於 nums[right]，所以可以在更前面檔掉
            # if nums[left] == nums[mid] == nums[right]:
            #     left += 1
            #     right -= 1
            # 所以當 nums[left] == nums[mid]時，只要不會出現 nums[left] == nums[mid] == nums[right]的情況，就一定是有序的
        
                

        return False