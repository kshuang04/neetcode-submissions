class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        n = len(isConnected)
        num_provinces = 0

        def bfs(city):
            stack = [city]
            while stack:
                top = stack.pop()
                visited.add(top)
                for i in range(n):
                    if isConnected[top][i] == 1 and i not in visited:
                        stack.append(i)

        for i in range(n):
            if i not in visited:
                bfs(i)
                num_provinces += 1
        
        return num_provinces