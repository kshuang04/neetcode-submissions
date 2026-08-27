class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num_provinces = 0
        n = len(isConnected)
        visited = set()

        def dfs(city):
            stack = [city]
            visited.add(city)

            while stack:
                curr = stack.pop()
                for i in range(n):
                    if isConnected[curr][i] == 1 and i not in visited:
                        stack.append(i)
                        visited.add(i)

        for i in range(n):
            if i not in visited:
                num_provinces += 1
                dfs(i)
        
        return num_provinces