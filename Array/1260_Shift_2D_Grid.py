class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        size = m * n

        # 思路：將 2D 座標展平成 1D 索引，右移 k 次後再還原為 2D 座標
        
        def to_idx_1d(i, j):
            # 將 2D 座標 (i, j) 轉換成 1D 索引
            return i * n + j

        def to_idx_2d(a):
            # 將 1D 索引 a 轉換回 2D 座標 (i, j)
            i = a // n
            j = a % n
            return i, j

        output = [[-1 for _ in range(n)] for _ in range(m)]
        
        for i in range(0, m):
            for j in range(0, n):
                new_i, new_j = to_idx_2d((to_idx_1d(i, j) + k) % size) #注意轉成一維再shift k次後會超出邊界，故要mode size
                output[new_i][new_j] = grid[i][j]
                
        return output

class Solution2:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # 更快版本
        # 二維矩陣轉成一維矩陣
        m = len(grid)
        n = len(grid[0])
        size = m * n
        elements = [grid[i][j] for i in range(m) for j in range(n)]
        # 移動k次
        k = k % size
        # ex. k = 2, [1, 2, 3, 4, 5] -> [4, 5, 1, 2, 3]
        elements = elements[-k:] + elements[:size - k]
        # 轉回二維
        return [[elements[i*n + j] for j in range(n)] for i in range(m)]
    
    
    
    