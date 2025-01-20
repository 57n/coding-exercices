class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        '''
        這題無法使用 Binary Search（⼆分搜尋）來解決。

        原因分析
        
        Binary Search 適用於 單調遞增或單調遞減 的序列，透過每次將搜尋範圍對半縮小來找到目標元素，時間複雜度為 O(log n)。
        
        而這題的條件是判斷是否為 山形陣列（Mountain Array），需要同時滿足以下兩個條件：
            1.	嚴格遞增：存在某個峰值索引i，使得 arr[0] < arr[1] < … < arr[i] 
            2.	嚴格遞減：且  arr[i] > arr[i + 1] > … > arr[n - 1] 
        
        特點：
            •	序列不是單調的，而是先遞增後遞減，這種變化使得 Binary Search 不適用於整體檢查。
            •	Binary Search 適合查找元素或峰值，但這題需要檢查整體結構是否符合山形規則。
        
        但是：可以用 Binary Search 找峰值
        
        如果只是要找到峰值（最大值的位置），那可以用 Binary Search，但無法直接判斷是否為山形陣列。
        
        核心問題：
            •	Binary Search 找到峰值後，還需要遍歷檢查兩邊是否分別嚴格遞增與遞減，這樣會導致時間複雜度回到 O(n)。
        
        正確的解法（線性掃描）
        
        最簡單、最高效的方式是線性掃描，時間複雜度為 O(n)。

        結論
            •	Binary Search 不適用：因為整體不是單調序列。
            •	正確方法：使用線性掃描，效率高且邏輯清楚。
            •	如果強行使用 Binary Search 找峰值，還需額外檢查兩側遞增/遞減，無法降低總體時間複雜度。
        
        所以這題直接用線性掃描是最合理的選擇。
        '''

        # 可以優化加速的部分，長度小於3就return
        n = len(arr)
        if n < 3:
            return False  # 長度不足

        i = 0
        # 先掃描嚴格遞增
        while i < len(arr) - 1 and arr[i] < arr[i+1]:
            i += 1

        if i == 0 or i == len(arr) - 1:
            # 掃完嚴格遞增後，如果 i 是在arr的頭，或是尾巴，代表不符合 Mountain Array的定義
            return False

        # 掃描嚴格遞減
        while i < len(arr) - 1 and arr[i] > arr[i+1]:
            i += 1

        if i < len(arr) - 1: # 沒有走到底，代表不符合 Mountain Array 的定義
            return False

        return True
        