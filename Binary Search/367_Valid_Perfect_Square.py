class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 理論上要從 1....找到√num
        # 但題目說You must not use any built-in library function, such as sqrt.
        # 所以就是在不知道√num的情況下，用binary search從1找到num，看能不能找到一個mid，使得 mid * mid = num
        # 使用標準binary search模板
        left = 1
        right = num

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num: # 如果平方小於 num，表示 mid 偏小，範圍需要右移
                left = mid + 1
            else: # 如果平方大於 num，表示 mid 偏大，範圍需要左移
                right = mid - 1
        return False # 最後找不到就是沒有
        