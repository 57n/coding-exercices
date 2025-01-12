class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left = 0
        right = len(arr) - 1
        """
        請注意，解題時一開始可能會碰到想要比較arr[mid] 和 arr[mid-1]之間的關係狀況，但發現會需要寫
        left = mid 時就需要注意了，因為會進入無窮迴圈，此時發現比較 arr[mid] 和 arr[mid-1]不可行
        應該改成比較arr[mid] 和 arr[mid+1]
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid-1]: # 右邊比較大，往右移找
                left = mid # <- 這裡可能導致無窮迴圈
            else:
                # mid == 0 or nums[mid] < nums[mid-1]
                # arr is guaranteed to be a mountain array. 所以沒有arr[mid] == arr[mid-1]等於的狀況
                right = mid - 1
        """
        while left < right: # 希望最後收斂在left==right，此時arr[left]是peak，故不用 while left <= right
            mid = (left + right) // 2
            if arr[mid] < arr[mid+1]: # 右邊比較大，往右移找
                left = mid + 1
            else:
                # arr[mid] > arr[mid+1]
                # arr is guaranteed to be a mountain array. 所以沒有arr[mid] == arr[mid-1]等於的狀況
                right = mid # mid有可能是peak，所以不能用 right = mid - 1
                
        return left