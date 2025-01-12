# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 找第一個符合條件的 Bad Version，可以視為找最左邊界
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            if not isBadVersion(mid): # 代表第一個 bad version 在右邊， mid 要往右移
                left = mid + 1
            else: # 代表第一個 bad version 在左邊， mid 要往左移
                right = mid - 1

            # 最後一次進入迴圈時，left 一定 == right，此時mid=left=right，如果 mid 不是bad version，left往右移，就一定是bad version
            # 如果mid是bad version，right往左移，right就會是bad version的前一個，left則會保持在第一個bad version
        return left
        