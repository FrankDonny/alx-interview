#!/usr/bin/python3
"""making change"""


def makeChange(coins, total):
    """function of make change"""
    if total <= 0:
        return 0

    table = [float('inf')] * (total + 1)
    table[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            table[i] = min(table[i], table[i - coin] + 1)

    if table[total] == float('inf'):
        return -1
    else:
        return table[total]
