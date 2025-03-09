class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 解題思路：
        # 1. 先把前面跟 newInterval 沒有重疊的區間加進去 final list
        # 2. 再把跟 newInterval 有重疊的區間統統合併
        # 3. 最後把後面跟 newInterval 沒有重疊的區間加進去 final list

        result = []
        n = len(intervals)

        i = 0
        
        # intervals[i]的尾端，跟 newInterval 的頭端沒有碰到，就是沒有跟 newInterval 重疊的區間
        # 當前 interval 的結束時間 < newInterval 的開始時間 => 完全在左邊，不會重疊
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # 這裡都會是跟 newInterval 重疊的區間，intervals[i]的頭端沒有超出 newInterval 的尾端，就是有重疊
        # 當前 interval 的開始時間 <= newInterval 的結束時間 => 代表重疊，需要合併
        # 這裡的條件請畫圖想一下會比較好
        # merged_interval = newInterval
        # while i < n and intervals[i][0] <= newInterval[1]:
        #     merged_interval = [min(intervals[i][0], merged_interval[0]), max(intervals[i][1], merged_interval[1])]
        #     i += 1
        # 註解部分是我之前寫法，這裡可以改成直接更新 newInterval 區間就好，可以省空間
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        result.append(newInterval)

        # 把剩下的 interval 加進去
        while i < n:
            result.append(intervals[i])
            i += 1

        return result