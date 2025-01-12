class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def eating_hours(bananas, k):
            total_hours = sum([(banana + k - 1) // k for banana in bananas])
            return total_hours

        # 吃香蕉最慢速度是1，一小時一根
        # 最大速度是 max(piles)，再超過需要的時間也不會減少

        # 思路：用binary search在 1 ~ max(piles)之間找到最小的速度k，使得KoKo可以在h小時吃完香蕉
        # 找到「最小」符合條件的k => 套用最左邊界問題的模板
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            if eating_hours(piles, mid) > h:
                left = mid + 1 # 代表吃太慢，需要的小時算出來 > h，所以吃的速度要提升，往右移
            else:
                # 代表花的時間 <= h
                # 注意當花的時間 == h 時，我們仍然要往左移，因為目標是要找到最小的k
                right = mid - 1

        # 最後一次迴圈時會處在left == right == mid
        # 此時用每小時吃mid跟香蕉的速度，發現還是大於h小時的話，left往右移一步，就會來到 <= h小時的最左邊界
        # 若發現是小於等於h小時的話，代表left已經處在最左邊界了，此時left不會動，right往左邊移，right就會離開最左邊界，此時right = left - 1
        # 所以我們要返回left而不是right

        return left
        