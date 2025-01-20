class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 一般想法在做 merge sorted array的時候，通常會開一個新的array，然後用雙指針的方式從index 0開始merge
        # 但是這題要求 modify nums1 in-place instead，所以不能開新的array，只能使用原本的nums1
        # 如果從index 0開始填nums1，那就可能會把nums1前面的數字洗掉
        # 不過這題可以看到有先把 nums1 最終所需空間開好，後面還沒補上的地方都是0，因此可以換個思路
        # 從array的尾巴開始填數字，倒著填回去，就不會洗掉nums1原本的數字了！

        pointer1 = m - 1
        pointer2 = n - 1
        
        idx = m + n - 1
        while pointer1 >= 0 and pointer2 >=0:
            if nums1[pointer1] > nums2[pointer2]:
                nums1[idx] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[idx] = nums2[pointer2]
                pointer2 -= 1
            idx -= 1

        while pointer2 >= 0:
            nums1[idx] = nums2[pointer2]
            pointer2 -= 1
            idx -= 1