class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        解法1，最簡單直觀的in-place sorting，使用counting sort。計算有多少個0, 1, 2，然後再直接修改array
        '''
        count_0 = 0
        count_1 = 0

        for n in nums:
            if n == 0:
                count_0 += 1
            elif n == 1:
                count_1 += 1

        i = 0
        while count_0 > 0:
            nums[i] = 0
            count_0 -= 1
            i += 1
        
        while count_1 > 0:
            nums[i] = 1
            count_1 -= 1
            i += 1

        # 剩下的都給2
        while i < len(nums):
            nums[i] = 2
            i += 1

class Solution2:
    def sortColors(self, nums):
        '''
        使用Dutch National Flag Algorithm（荷蘭國旗問題）
        目標：
            - 將數組內的 0、1、2 按順序排列，並做到 in-place 操作（不使用額外空間）

        核心思路：
            1. 使用雙指針：
            - `left` 指向 0 應該放置的位置
            - `right` 指向 2 應該放置的位置
            - `i` 遍歷整個數組，找到 0 和 2 時與正確位置交換
        '''

        i = 0 # i用來遍歷整個數組nums
        left = 0 # left 指向 0 應該放置的位置
        right = len(nums) - 1 # right 指向 2 應該放置的位置

        while i <= right: # 注意當 i == right時，還是要比對，因為nums[right]可能會是0, 1, 2都有
            if nums[i] == 0:
                # 找到 0 時，nums[left]和nums[i]交換
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 1:
                # 不做變動，i繼續前進
                i += 1
            else:
                # nums[i] == 2時，nums[right]和nums[i]交換
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                # 此時 i 不前進，因為換過去後nums[i]可能會是0, 1, 2都有，還需要再被檢查

        '''
        當 nums[i] == 0：
        - 因為 i 永遠 >= left，所以nums[left] 位置的數字要麼是 0 或 1（因為沿途上 2 已被移到右邊）。
        - 與 nums[left] 交換後，nums[i] 位置一定是安全的（0 或 1），所以 i 可以前進。
        - 兩種可能情況：
        - 如果 nums[i] == 0 且 nums[left] == 0，則 i == left，此時交換自己，不影響順序 (不可能會有 nums[i] == 0 and nums[left] == 0 ，此時 i != left 的情況。由於 left 只會在 nums[i] == 0 時才會移動，因此當 nums[left] == 0 時，left 和 i 必然相等，意味著交換操作發生在相同位置，也就是 i == left。）
        - 如果 nums[i] == 0 且 nums[left] == 1，則 i > left，nums[left] 和 nums[i] 之間的數字一定是1，交換後 i 可前進，left 位置正確

        當 nums[i] == 2：
        - nums[right] 位置的數字可能是 0、1 或 2（因為尚未檢查過），交換後的 nums[i] 可能仍是 2。
        - 交換完後，需重新檢查當前 nums[i]，因此 i 不能前進。
        '''