class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 1
        right = x

        while left <= right:
            mid = (left+right) // 2
            if mid * mid == x:
                return mid # 把等於狀況單獨出來寫，這樣比較好記
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        # 找不到存在的整數時，就變成最右邊界問題（最大的整數）
        # 記憶：找最大值(最右邊界) return right
        # 找最小值(最左邊界以及插入位置) return left
        # 找最大值就需要left一直增加，最後left會 > right，就超出去了，這時候right才是正確的 
        return right