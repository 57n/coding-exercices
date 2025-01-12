class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        # 先看總和是10個(偶數個) elements的例子
        # ex. nums1 = [1,3,5,7,9]
        # ex. nums2 = [2,4,6,8,10]
        # 找到一個切斷點，使得 max(nums1_left, nums2_left) <= min(num1_right, nums2_right)
        # 請注意，切斷點要讓左邊的element數量 == 右邊的element數量，因為總和數量是偶數
        # nums1 = [1, 3 | 5, 7, 9] <- 切了兩個element在左邊，我們定義cut_point = 2
        # nums2 = [2, 4, 6 | 8, 10] <- 因為總共有10個element，所以nums2左邊要切三個，這樣才平衡，num1+num2左邊總共5個，num1+num2右邊也有五個
        # 此時 max(nums1_left, nums2_left) = 6  min(num1_right, nums2_right) = 5
        # 6 > 5, 不符合 max(nums1_left, nums2_left) <= min(num1_right, nums2_right)的情況，要重切
        # 正確切點： nums1 = [1, 3, 5 | 7, 9]
        #          nums2 = [2, 4 | 6, 8, 10]
        # 此時 max(nums1_left, nums2_left) = 5  min(num1_right, nums2_right) = 6
        # 符合條件，所以中位數是 (5 + 6) / 2 = 5.5

        # 再來我們看總和是11個(偶數個) elements的例子
        # ex. nums1 = [1,3,5,7,9,11]
        # ex. nums2 = [2,4,6,8,10]
        # 這時我們設計切斷點要讓左邊的element數量 + 1 == 右邊的element數量，因為總和數量是奇數
        # 正確切點： nums1 = [1, 3, 5 | 7, 9, 11] <- 切了三個element在左邊，切斷點 = 3
        #          nums2 = [2, 4, 6 | 8, 10] <- 因為總共有11個element，所以nums2左邊要切 3 個，此時num1+num2左邊總共6個，num1+num2右邊會有5個
        # 此時 max(nums1_left, nums2_left) = 6  min(num1_right, nums2_right) = 7
        # 6 <= 7 符合條件，這時返回中位數 6

        
        '''
        max(nums1_left, nums2_left) <= min(num1_right, nums2_right) 這件事情
        更精確說是 nums1_left_max <= nums2_right_min and nums2_left_max <= num1_right_min
        因為nums1_left_max本來就必定 <= nums1_right_min，nums2_left_max 本來就必定 <= num2_right_min
        能夠明白實際精確寫法是 nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min 會比較好分析binary search mid往左移右移的條件
        '''
        
        left = 0
        # 我們定義 cutting_point = 0 意思是左邊會有 0 個element，cutting_point = n 是左邊有 n 個element，所以左邊最多會有len(nums1)個element，故right不是len(nums1)-1
        right = len(nums1)

        total_element_num = len(nums1) + len(nums2)

        while left <= right:
            mid = (left + right) // 2 # mid作為切斷點

            cutting_point_1 = mid
            #nums1_left_max = max(nums1[:cutting_point_1]) if cutting_point_1 > 0 else float("-inf")
            #nums1_right_min = min(nums1[cutting_point_1:]) if cutting_point_1 < len(nums1) else float("inf")
            # 以下比用min max更快
            nums1_left_max = nums1[cutting_point_1 - 1] if cutting_point_1 > 0 else float("-inf")
            nums1_right_min = nums1[cutting_point_1] if cutting_point_1 < len(nums1) else float("inf")

            cutting_point_2 = (total_element_num + 1) // 2 -  cutting_point_1 # 總共10個，那麼左邊要拿5個；總共11個左邊要拿6個
            #nums2_left_max = max(nums2[:cutting_point_2]) if cutting_point_2 > 0 else float("-inf")
            #nums2_right_min = min(nums2[cutting_point_2:]) if cutting_point_2 < len(nums2) else float("inf")
            # 以下比用min max更快
            nums2_left_max = nums2[cutting_point_2 - 1] if cutting_point_2 > 0 else float("-inf")
            nums2_right_min = nums2[cutting_point_2] if cutting_point_2 < len(nums2) else float("inf")

            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                if total_element_num % 2 == 1: # 總數是奇數個
                    return float(max(nums1_left_max, nums2_left_max))
                else:
                    # 總數是偶數個
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
            elif nums1_left_max > nums2_right_min:
                # nums1 = [1, 3 | 5, 7, 9]
                # nums2 = [2, 4, 6 | 8, 10]
                # 請注意，當 nums1 左邊有越多 elements，nums1_left_max會變大，nums2左邊的 element就會變少 -> nums2 右邊 elements會變多，nums2_right_min就會越小
                # 所以這時我們可以比較 nums1_left_max 是否 <= nums2_right_min
                # 若 nums1_left_max > nums2_right_min，代表我們給 nums1 左邊太多 elements，此時cutting_point_1應該要向左移
                right = mid - 1
            elif nums2_left_max > nums1_right_min:
                # 當 nums1 左邊有越少 elements，nums1 右邊 elements會變多，nums1_right_max就會變小 -> nums2左邊的 element就會變多，nums1_left_max會變大
                # 所以這時我們可以比較 nums2_left_max 是否 <= nums1_right_min
                # 若 nums2_left_max > nums1_right_min，代表我們給 nums1_right_max 太多 elements，此時cutting_point_1應該要向右移
                left = mid + 1