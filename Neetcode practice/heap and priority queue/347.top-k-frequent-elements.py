import heapq

# heapq会首先比较元组的第一项，如果第一项相同，则比较第二项，依此类推
class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        # 最小堆中的元素为(频率，元素)，按频率来排序
        heap = []
        for num, freq in count.items():
            # 如果堆的大小小于k，直接添加
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                # 如果当前元素的频率大于堆顶元素的频率，则弹出堆顶元素，并添加当前元素
                if freq > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (freq, num))

        # 堆中的元素就是前k个高频元素
        return [num for freq, num in heap]
