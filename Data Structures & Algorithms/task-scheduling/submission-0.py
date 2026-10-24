class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap= [-count for count in freq.values()]
        heapq.heapify(heap)
        time = 0
        while heap:
            temp = []
            cycle = n + 1
            while cycle > 0 and heap:
                count = -heapq.heappop(heap)
                if count > 1:
                    temp.append(-(count-1))
                time += 1
                cycle -= 1
            for count in temp:
                heapq.heappush(heap, count)
            if heap:
                time += cycle
        return time
        