```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```
# > 只要涉及递归，都可以抽象成二叉树的问题。
# ! 二叉树前序遍历 框架
```python
def traverse(root):
    if root is None:
        return
    # 前序遍历的代码位置
    traverse(root.left)
    # 中序遍历的代码位置
    traverse(root.right)
    # 后续遍历的代码位置

```

# > 快速排序就是个二叉树的前序遍历，
'''
快速排序的逻辑是，若要对nums[lo..hi]进行排序，
我们先找一个分界点p，通过交换元素使得nums[lo..p-1]都小于等于nums[p]，
且nums[p+1..hi]都大于nums[p]，
然后递归地去nums[lo..p-1]和nums[p+1..hi]中寻找新的分界点，
最后整个数组就被排序了。

'''
```python
def sort(nums, lo, hi):
    # ****** 前序遍历位置 ******
    # 通过交换元素构建分界点 p
    p = partition(nums, lo, hi)
    # ************************
    sort(nums, lo, p - 1)
    sort(nums, p + 1, hi)

```
# > 归并排序就是个二叉树的后续遍历，
'''
再说说归并排序的逻辑，若要对nums[lo..hi]进行排序，
我们先对nums[lo..mid]排序，再对nums[mid+1..hi]排序，
最后把这两个有序的子数组合并，整个数组就排好序了。
'''
```python
def sort(nums, lo, hi):
    mid = (lo + hi) // 2
    sort(nums, lo, mid)
    sort(nums, mid + 1, hi)
    # ****** 后序遍历位置 ******
    # 合并两个排好序的子数组
    merge(nums, lo, mid, hi)
    # ************************

```
# > 二叉树的算法思想的运用广泛，甚至可以说，只要涉及递归，都可以抽象成二叉树的问题。
# > 写递归算法的关键是要明确函数的「定义」是什么，然后相信这个定义，利用这个定义推导最终结果，绝不要试图跳入递归。
# > 写树相关的算法，简单说就是，先搞清楚当前root节点该做什么，
# > 然后根据函数定义递归调用子节点，递归调用会让孩子节点做相同的事情。

# > 比如说让你计算一棵二叉树共有几个节点：

# 定义：count(root) 返回以 root 为根的树有多少节点
```python
def count(root):
    # base case
    if root is None:
        return 0
    # 自己加上子树的节点数就是整棵树的节点数
    return 1 + count(root.left) + count(root.right)

```
# > 例题 1. LeetCode 226.翻转二叉树
'''
     4
   /   \
  2     7
 / \   / \
1   3 6   9

算法原地翻转二叉树，使得以root为根的树变成：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
```

# > 例题 1. 翻转二叉树
# 将整棵树的节点翻转
#! 关键思路在于我们发现翻转整棵树就是交换每个节点的左右子节点，
#! 于是我们把交换左右子节点的代码放在了前序遍历的位置。
```python
def invert_tree(root):
    # base case
    if root is None:
        return None

    # **** 前序遍历位置 ****
    # root 节点需要交换它的左右子节点
    root.left, root.right = root.right, root.left

    # 让左右子节点继续翻转它们的子节点
    invert_tree(root.left)
    invert_tree(root.right)

    return root

```
# > 例题2. 填充二叉树节点的右侧指针
# 主函数
```python
def connect(root):
    if root is None:
        return None
    connect_two_node(root.left, root.right)
    return root
```

# 定义：输入两个节点，将它俩连接起来

```python
def connect_two_node(node1, node2):
    if node1 is None or node2 is None:
        return

    # **** 前序遍历位置 ****
    # 将传入的两个节点连接
    node1.next = node2

    # 连接相同父节点的两个子节点
    connect_two_node(node1.left, node1.right)
    connect_two_node(node2.left, node2.right)
    # 连接跨越父节点的两个子节点
    connect_two_node(node1.right, node2.left)

```
# > 例题3. 将二叉树展开为单链表
# 定义：将以 root 为根的树拉平为链表
```python
def flatten(root):
    # base case
    if root is None:
        return

    flatten(root.left)
    flatten(root.right)

    # **** 后序遍历位置 ****
    # 1、左右子树已经被拉平成一条链表
    left = root.left
    right = root.right

    # 2、将左子树作为右子树
    root.left = None
    root.right = left

    # 3、将原先的右子树接到当前右子树的末端
    p = root
    while p.right is not None:
        p = p.right
    p.right = right
```

# > 递归算法的关键要明确函数的定义，相信这个定义，而不要跳进递归细节。
# > 写二叉树的算法题，都是基于递归框架的，我们先要搞清楚root节点它自己要做什么，
# > 然后根据题目要求选择使用前序，中序，后续的递归框架。
