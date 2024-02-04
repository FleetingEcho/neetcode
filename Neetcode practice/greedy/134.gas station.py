def canCompleteCircuit(gas, cost):
    len_gas = len(gas)
    spare = 0
    minSpare = float('inf')
    minIndex = 0

    for i in range(len_gas):
        spare += gas[i] - cost[i]
        if spare < minSpare:
            minSpare = spare
            minIndex = i

    return (minIndex + 1) % len_gas if spare >= 0 else -1


#如果最后一个加油站是最佳起点的前一个加油站，(minIndex + 1) % len_gas将会正确地返回0
#即数组的第一个加油站。
