class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num_provinces = 0
        n = len(isConnected)
        visited = set()

        def dfs(city):
            stack = [city]
            while stack:
                curr_city = stack.pop()
                visited.add(curr_city)
                for i in range(n):
                    if isConnected[curr_city][i] == 1 and i not in visited:
                        stack.append(i)

        for i in range(n):
            if i not in visited:
                num_provinces += 1
                dfs(i)
                    
        return num_provinces