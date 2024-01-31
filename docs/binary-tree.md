
二叉树算法的设计的总路线：明确一个节点要做的事情，
然后剩下的事抛给框架。


二叉树的增删改查 + 前中后序遍历
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BST遍历框架
def BST(root, target):
    if root is None:
        return None
    if root.val == target:
        # 找到目标，做点什么
        pass
    if root.val > target:
        BST(root.left, target)
    if root.val < target:
        BST(root.right, target)


#===========================================
如何判断我们应该用 前序 还是 中序 还是 后序遍历 的框架
#! 652 题「寻找重复子树」
# 寻找重复子树
def find_duplicate_subtrees(root):
    memo = {}
    res = []

    def traverse(root):
        if root is None:
            return '#'
        left = traverse(root.left)
        right = traverse(root.right)
        subTree = f"{left},{right},{root.val}"
        freq = memo.get(subTree, 0)
        if freq == 1:
            res.append(root)
        memo[subTree] = freq + 1
        return subTree

    traverse(root)
    return res

# 二叉树所有节点值加一
#> 1. 如何把二叉树所有的节点中的值加一？
def plus_one(root):
    if root is None:
        return
    root.val += 1
    plus_one(root.left)
    plus_one(root.right)
```


```python

def find_duplicate_subtrees(root):
    memo = {}  # 记录所有子树以及出现的次数
    res = []   # 记录重复的子树根节点

    def traverse(root):
        if root is None:
            return '#'

        left = traverse(root.left)
        right = traverse(root.right)

        sub_tree = f'{left},{right},{root.val}'
        freq = memo.get(sub_tree, 0)
        if freq == 1:
            res.append(root)  # 多次重复也只会被加入结果集一次

        memo[sub_tree] = freq + 1  # 给子树对应的出现次数加一
        return sub_tree

    traverse(root)
    return res  # 返回的是TreeNode形式

# 示例使用：
# root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(2, TreeNode(4)), TreeNode(4)))
# print(find_duplicate_subtrees(root))
```


// > 二叉树的序列化操作

```python
def traverse(root):
	#对于空节点，可以用一个特殊字符表示
    if root is None:
        return '#'
		#将左右子树序列化成字符串
    left = traverse(root.left)
    right = traverse(root.right)
		#后序遍历代码位置
		#左右子树加上自己，就是以自己为根的二叉树序列化结果
    sub_tree = f'{left},{right},{root.val}'
    return sub_tree

```

 > 2. 如何判断两棵二叉树是否完全相同？

```python
# 判断两棵二叉树是否完全相同
def is_same_tree(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.val != root2.val:
        return False
    return is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right)

```

判断 BST 的合法性、增、删、查。其中「删」和「判断合法性」略微复杂

 ! 个二叉树中，任意节点的值要大于左子树所有节点的值，且要小于右边子树的所有节点的值。

零、判断 BST 的合法性

```python
# 判断BST的合法性
# 加入了对左右子树的完整判断
def is_valid_BST(root, min_val=None, max_val=None):
    if root is None:
        return True
    if min_val is not None and root.val <= min_val: #根>左子树
        return False
    if max_val is not None and root.val >= max_val: #根<右子树
        return False
    return is_valid_BST(root.left, min_val, root.val) and is_valid_BST(root.right, root.val, max_val)

```

BST 的定义，root 需要做的，不仅仅是和左右子节点比较，而是要和左子树和右子树的所有节点比较。
这种情况，我们可以使用辅助函数，增加函数参数列表，在参数中携带额外信息.

      20
     /  \
    8    10
   / \   / \
  3   5  9 18
             \
             22


在 BST 中查找一个数是否存在

```python
# 在BST中查找一个数是否存在
def is_in_BST(root, target):
    if root is None:
        return False
    if root.val == target:
        return True
    elif target < root.val:
        return is_in_BST(root.left, target)
    else:
        return is_in_BST(root.right, target)
```

 在 BST 中插入一个数

```python
def insert_into_BST(root, val):
    if root is None:
        return TreeNode(val)
    if root.val < val:
        root.right = insert_into_BST(root.right, val)
    elif root.val > val:
        root.left = insert_into_BST(root.left, val)
    return root

```


在 BST 中删除一个数    ---删除节点的同时不能破坏 BST 的性质。有三种情况

情况 1：A 恰好是末端节点，两个子节点都为空，则直接删除

情况 2：A 只有一个非空子节点，那么它要让这个孩子接替自己的位置。

情况3： A 有两个子节点，麻烦了，为了不破坏 BST 的性质，
A 必须找到左子树中最大的那个节点，或者右子树中最小的那个节点来接替自己。


```python
# 在BST中删除一个数
def delete_node(root, key):
    if root is None:
        return None
    if root.val == key:
			# 这两个if 把情况1和2都正确处理了
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
			# 处理情况3
        min_node = get_min(root.right)
        root.val = min_node.val
        root.right = delete_node(root.right, min_node.val)
    elif root.val > key:
        root.left = delete_node(root.left, key)
    else:
        root.right = delete_node(root.right, key)
    return root

def get_min(node):
	# BST最左边的就是最小的
    while node.left is not None:
        node = node.left
    return node
```


> 1. 二叉树算法设计的总路线：把当前节点要做的事做好，其他的交给递归框架，不用当前节点操心。

> 2. 如果当前节点会对下面的子节点有整体性影响，可以通过辅助函数加长参数列表，借助函数参数传递信息。
   这就是递归函数传递信息的常用方式。
> 3. 在二叉树框架之上，扩展出一套 BST 遍历框架：

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def BST(root, target):
    if root is None:
        return None

    if root.val == target:
        # 找到目标，做点什么
        pass
    elif root.val < target:
        BST(root.right, target)
    elif root.val > target:
        BST(root.left, target)

# 示例使用：
# root = TreeNode(2, TreeNode(1), TreeNode(3))
# BST(root, 3)
```

> 4. 掌握BST 的基本操作，包括判断 BST 的合法性以及 BST 中的增、删、查操作。

