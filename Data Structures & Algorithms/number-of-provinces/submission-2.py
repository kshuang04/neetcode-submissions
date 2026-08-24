class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num_provinces = 0
        visited = set()
        n = len(isConnected)

        def dfs(city):
            stack = [city]
            visited.add(city)

            while stack:
                top = stack.pop()

                for i in range(n):
                    if isConnected[top][i] == 1 and i not in visited:
                        stack.append(i)
                        visited.add(i)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i not in visited:
                    dfs(i)
                    num_provinces += 1
        
        return num_provinces