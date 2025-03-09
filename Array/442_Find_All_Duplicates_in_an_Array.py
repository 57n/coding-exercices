class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # 題目說len(nums) = n，而且數字範圍是[1, n]，可以保證是正整數
        # 題目要求要O(1)空間，這題可以用 數組索引標記法 (In-Place Index Marking) 來做
        '''
        思路：如果碰到數字a，那就把nums[a-1]的位置的數值變成 -1 * nums[a-1]，
        當下次又碰到a時，會發現 nums[a-1] 是負數，我們就知道a是duplicate （題目說每個數字最多只會出現兩次）
        '''
        result = []

        for n in nums:
            n = abs(n) # 因為有可能被別人改成負數，用abs轉正
            if nums[n-1] < 0:
                result.append(n)
            else:
                nums[n-1] = -1 * nums[n-1]
        return result
        