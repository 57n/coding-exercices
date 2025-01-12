class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Follow up:

        # What if the given array is already sorted? How would you optimize your algorithm?
        nums1.sort()
        nums2.sort()

        # 雙指針法
        pointer1 = 0
        pointer2 = 0

        output = []

        # 如果已經是sorted的話，時間複雜度是O(min(m, n))（雙指針遍歷），空間複雜度是O(1)
        while pointer1 < len(nums1) and pointer2 < len(nums2):
            if nums1[pointer1] == nums2[pointer2]:
                output.append(nums1[pointer1]) # 一樣的話代表找到，兩邊都各加1
                pointer1 += 1
                pointer2 += 1
            elif nums1[pointer1] < nums2[pointer2]: 
                pointer1 += 1 # 比較小的要加1
            else:
                pointer2 += 1
        return output
        # What if nums1's size is small compared to nums2's size? Which algorithm is better?
        # 優化策略是將nums1 儲存在字典中（因為 nums1 更小，字典的空間占用更少），然後遍歷 nums2
        # 時間複雜度是O(m+n) 空間複雜度是 O(min(m,n))
        # if len(nums1) > len(nums2):
        #     nums1, nums2 = nums2, nums1
        # counts = {}
        # for i in nums1:
        #     if i in counts:
        #         counts[i] += 1
        #     else:
        #         counts[i] = 1
        # output = []
        # for j in nums2:
        #     if j in counts and counts[j] > 0:
        #         counts[j] -= 1
        #         output.append(j)
        # return output
        
        # What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
        # 當 nums2 太大（例如儲存在硬碟中）時，可以將問題轉化為「流處理問題」：
        # 1.	將較小的數組（nums1）存入字典。
        # 2.	對 nums2 進行「塊讀取」（chunk-wise processing）。
        # 3.	每次讀取一部分 nums2，與字典進行匹配並更新結果。
            