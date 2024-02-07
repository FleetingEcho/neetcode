import heapq
import queue
class Solution:
  def minMeetingRooms(intervals):
      if not intervals:
          return 0

      # start time
      intervals.sort(key=lambda x: x[0])

      # save end time
      rooms =queue.PriorityQueue()
      rooms.put(intervals[0][1])

      for i in range(1, len(intervals)):
          if intervals[i][0] >= rooms.queue[0]:
              rooms.get()
          rooms.put(intervals[i][1])
      return rooms.qsize()


#如果用heap
class Solution:
  def minMeetingRooms(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])

    rooms = []
    heapq.heappush(rooms, intervals[0][1]) #默认最小堆

    for i in range(1, len(intervals)):
        if intervals[i][0] >= rooms[0]:
            heapq.heappop(rooms)
        heapq.heappush(rooms, intervals[i][1])
    return len(rooms)