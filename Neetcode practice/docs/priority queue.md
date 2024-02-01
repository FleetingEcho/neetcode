```python
优先级越小越先出队，如果put传入元组，则会根据元组的第一个元素决定出队顺序

from queue import PriorityQueue


queue.put(item):

功能：将 item 放入队列。
参数：
item：要放入队列的项


queue.get():

功能：从队列中移除并返回一个元素。

queue.qsize():

功能：返回队列中大致的元素数量。注意，这个数量不一定完全准确，因为在返回结果和使用结果之间，队列中的项可能被其他线程添加或移除。

queue.empty():

功能：检查队列是否为空。如果队列为空，返回 True；否则返回 False。同样，这个结果可能不完全准确。

queue.full():
功能：检查队列是否已满。如果队列已满，返回 True；否则返回 False。

queue.put_nowait(item):

功能：相当于 put(item, False)。尝试立即将 item 放入队列，如果队列已满，则引发 queue.Full 异常。

queue.get_nowait():

功能：相当于 get(False)。尝试立即从队列中取出一个元素，如果队列为空，则引发 queue.Empty 异常。


queue.join():

功能：阻塞直到队列中的所有项都被处理。处理项的方式是在完成工作后调用 task_done() 方法。

queue.task_done():

功能：用于指示之前由 get() 取出的一个任务已经完成。每个 get() 调用后都应有一个对应的 task_done() 调用。

PriorityQueue 在多线程程序中非常有用，因为它能确保线程安全地访问队列。当多个线程需要共享和处理同一组数据时，PriorityQueue 提供了一种安全且有效的方式来处理数据项。
```



```python
from queue import PriorityQueue

# 创建优先级队列实例
pq = PriorityQueue()

# 向队列中添加元素，格式为 (priority, item)
pq.put((2, 'medium priority task'))
pq.put((1, 'high priority task'))
pq.put((3, 'low priority task'))

# 从队列中取出元素
while not pq.empty():
    item = pq.get()
    print(item)
```