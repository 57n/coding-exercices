class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0]) # 先按照每個區間的起始點進行排序，確保後續合併時順序正確
        merged_list = [intervals[0]] # 初始化結果列表，將第一個區間放入作為基準
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            # 取當前區間與 merged_list 最後一個區間的結束點比較
            if merged_list[-1][1] >= interval[0]: # 判斷是否有重疊（注意：等於時也算重疊）
                merged_list[-1] = [merged_list[-1][0], max(merged_list[-1][1], interval[1])] # 若重疊，將結束時間更新為兩者中較大的值
            else:
                # 沒有重疊，直接將當前區間加入結果列表
                merged_list.append(interval)
        return merged_list