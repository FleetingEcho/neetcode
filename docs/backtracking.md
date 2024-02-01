
求子集（subset），求排列（permutation），求组合（combination）
这几个问题都可以用回溯算法解决。


//! 回溯算法就一种简单粗暴的算法技巧，说白了就是一个暴力穷举算法，比如让你 用回溯算法求子集、全排列、组合，

以上，就是排列组合和子集三个问题的解法，总结一下：

> 1.子集问题可以利用数学归纳思想，假设已知一个规模较小的问题的结果，思考如何推导出原问题的结果。
>   也可以用回溯算法，要用 start 参数排除已选择的数字。

> 2.组合问题利用的是回溯思想，结果可以表示成树结构，
>   我们只要套用回溯算法模板即可，关键点在于要用一个 start 排除已经选择过的数字。

> 3.排列问题是回溯思想，也可以表示成树结构套用算法模板，
>   不同之处在于使用 contains 方法排除已经选择的数字.

对于这三个问题，关键区别在于回溯树的结构，不妨多观察递归树的结构，很自然就可以理解代码的含义了。

//> 1. 子集


输入 nums = [1,2,3]，你的算法应输出 8 个子集，包含空集和本身，顺序可以不同：

[ [],[1],[2],[3],[1,3],[2,3],[1,2],[1,2,3] ]

```python


! 回溯算法模板

result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.append(路径)
        return
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择



def subsets(nums):
    res = []

    def backtrack(nums, start, track):
        res.append(list(track))  # 与Array.from(track)等效
        # 注意i从start开始递增
        for i in range(start, len(nums)):
            # 做选择
            track.append(nums[i])
            # 回溯
            backtrack(nums, i + 1, track)
            # 撤销选择
            track.pop()

    track = []
    backtrack(nums, 0, track)
    return res

# 测试代码
print(subsets([1, 2, 3]))

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []

        def backtrack(start: int, track: List[int]) -> None:
            res.append(list(track))
            for index in range(start, len(nums)):
                track.append(nums[index])
                backtrack(index + 1, track)
                track.pop()

        backtrack(0, [])
        return res


```
//> 2.组合

输入两个数字 n, k，算法输出 [1..n] 中 k 个数字的所有组合。

vector<vector<int>> combine(int n, int k);
比如输入 n = 4, k = 2，输出如下结果，顺序无所谓，
但是不能包含重复（按照组合的定义，[1,2] 和 [2,1] 也算重复）：

[
 [1,2],
 [1,3],
 [1,4],
 [2,3],
 [2,4],
 [3,4]
]
这就是典型的回溯算法，k 限制了树的高度，n 限制了树的宽度，
直接套我们以前讲过的回溯算法模板框架就行了：

```python
def combine(n, k):
    res = []

    def backtrack(start, track):
        # 到达树的底部
        if len(track) == k:
            res.append(list(track))  # 需要深拷贝
            return
        # 注意 i 从 start 开始递增
        for i in range(start, n + 1):
            # 做选择
            track.append(i)
            backtrack(i + 1, track)
            # 撤销选择
            track.pop()

    backtrack(1, [])
    return res

# 测试代码
print(combine(4, 2))

```


// > 3. 排列问题

输入一个不包含重复数字的数组 nums，返回这些数字的全部排列。

vector<vector<int>> permute(vector<int>& nums);
比如说输入数组 [1,2,3]，输出结果应该如下，顺序无所谓，不能有重复：

[
 [1,2,3],
 [1,3,2],
 [2,1,3],
 [2,3,1],
 [3,1,2],
 [3,2,1]
]

回溯算法详解 中就是拿这个问题来解释回溯模板的。这里又列出这个问题，
是将「排列」和「组合」这两个回溯算法的代码拿出来对比。

```python
def permute(nums):
    res = []

    def backtrack(track):
        # 触发结束条件
        if len(track) == len(nums):
            res.append(list(track))  # 需要深拷贝
            return
        for i in range(len(nums)):
            # 排除track中已经选择过的数字
            if nums[i] in track:
                continue
            # 做选择
            track.append(nums[i])
            # 进入下一层决策树
            backtrack(track)
            # 取消选择
            track.pop()

    backtrack([])
    return res

# 测试代码
print(permute([1, 2, 3]))

```


//> 总结

回溯模板依然没有变，但是根据排列问题和组合问题画出的树来看，
排列问题的树比较对称，而组合问题的树越靠右节点越少。

在代码中的体现就是，
> 1.排列问题每次通过 contains 方法来排除在 track 中已经选择过的数字；
> 2.而组合问题通过传入一个 start 参数，来排除 start 索引之前的数字。


以上，就是排列组合和子集三个问题的解法，总结一下：

> 1.子集问题可以利用数学归纳思想，假设已知一个规模较小的问题的结果，思考如何推导出原问题的结果。也可以用回溯算法，要用 start 参数排除已选择的数字。

> 2.组合问题利用的是回溯思想，结果可以表示成树结构，我们只要套用回溯算法模板即可，关键点在于要用一个 start 排除已经选择过的数字。

> 3.排列问题是回溯思想，也可以表示成树结构套用算法模板，不同之处在于使用 contains 方法排除已经选择的数字，前文有详细分析，这里主要是和组合问题作对比。

对于这三个问题，关键区别在于回溯树的结构，不妨多观察递归树的结构，很自然就可以理解代码的含义了。




