#BFS

from collections import deque
from typing import List, Set

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 使用双端队列存储待访问的单词
        q = deque([beginWord])

        # 将单词列表转换为集合，便于快速查找和删除
        words = set(wordList)
        words.discard(beginWord)  # 从集合中移除起始单词

        # 如果目标单词不在单词列表中，直接返回0
        if endWord not in words:
            return 0

        # 初始化步数计数器
        step = 1

        # 当队列非空时，进行循环
        while q:
            len_q = len(q)  # 获取当前队列长度
            # 遍历当前队列中的所有单词
            for i in range(len_q):
                curWord = q.popleft()  # 从队列中弹出一个单词

                # 如果当前单词是目标单词，返回步数
                if curWord == endWord:
                    return step

                # 获取当前单词的所有合法邻居单词，并将它们加入队列
                for s1 in self.getNeighbour(curWord, words):
                    q.append(s1)

            # 更新步数
            step += 1

        # 如果队列为空，说明没有找到路径，返回0
        return 0

    def getNeighbour(self, curWord: str, words: Set[str]) -> List[str]:
        arr = []
        # 遍历当前单词的每一个字符
        for i in range(len(curWord)):
            # 尝试将当前字符替换为a到z中的任意一个字符
            for str in range(ord('a'), ord('z') + 1):
                c = list(curWord)  # 将当前单词转换为字符列表
                c[i] = chr(str)    # 替换字符
                testStr = ''.join(c)  # 将字符列表转换回字符串

                # 如果新单词在单词集合中，将其加入邻居列表，并从集合中移除
                if testStr in words:
                    arr.append(testStr)
                    words.remove(testStr)
        return arr  # 返回邻居列表




#clean version

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([beginWord])
        words = set(wordList)
        words.discard(beginWord)

        if endWord not in words:
            return 0
        step = 1

        while q:
            len_q = len(q)
            for i in range(len_q):
                curWord = q.popleft()
                if curWord == endWord:
                    return step

                for s1 in self.getNeighbour(curWord, words):
                    q.append(s1)

            step += 1

        return 0

    def getNeighbour(self, curWord: str, words: Set[str]) -> List[str]:
        arr = []
        for i in range(len(curWord)):
            for char_code in range(ord('a'), ord('z') + 1):
                #replace one char with current char
                str_list = list(curWord)
                str_list[i] = chr(char_code)
                testStr = ''.join(str_list)
                if testStr in words:
                    words.remove(testStr)
                    arr.append(testStr)
        return arr
