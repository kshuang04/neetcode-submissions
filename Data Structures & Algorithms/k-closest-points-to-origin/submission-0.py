class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [] # [distance: [x,y]]

        for x, y in points:
            distance = math.sqrt(x ** 2 + y ** 2)
            minHeap.append([distance, [x, y]])
        
        minHeap.sort(key=lambda x : x[0])

        result = []
        for i in range(k):
            result.append(minHeap[i][1])
        
        return result