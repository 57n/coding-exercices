class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        三次反轉法 (O(1) 空間)
        做法：
        k = 3
        1.	整個陣列反轉 → [1,2,3,4,5,6,7] → [7,6,5,4,3,2,1]
        2.	前 k 個元素反轉 → [7,6,5] → [5,6,7]
        3.	後 n-k 個元素反轉 → [4,3,2,1] → [1,2,3,4]
        4.	結果 → [5,6,7,1,2,3,4]
        """

        def reverse(left, right):
            # left為要反轉的index起點
            # right為要反轉的index終點
            while left < right:
                # 這樣交換就不需要額外空間
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        n = len(nums)
        k = k % n # 避免 k > len(nums) 的 case像是：nums = [-1]，k = 2 ，而且這樣可以跑比較快
        
        reverse(0, len(nums)-1) # 整個陣列反轉
        reverse(0, k-1) # 前 k 個元素反轉
        reverse(k, len(nums)-1) # 後 n-k 個元素反轉。注意後n-k個元素用index k ~ len(nums)-1最直觀