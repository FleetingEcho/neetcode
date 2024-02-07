class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        def get_next_num(num):
            total_sum = 0
            while num > 0:
                #商，余数
                num, digit = divmod(num, 10)
                total_sum += digit ** 2
            return total_sum

        def traverse(cur):
            if cur == 1:
                return True
            if cur in seen:
                return False
            seen.add(cur)
            next_num = get_next_num(cur)
            return traverse(next_num)

        return traverse(n)


#或者更简单的


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set([n])

        def check(num):
            _list = [int(_char)**2 for _char in str(num)]
            return sum(_list)

        while n!=1:
            n = check(n)
            if n in seen:
                return False
            seen.add(n)

        return True