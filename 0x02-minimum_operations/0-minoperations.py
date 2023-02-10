#!/usr/bin/python3
"""minimum operations module"""


def minOperations(n):
    """of relating to prime factorization"""
    operations = 0
    curr_len = 1
    while curr_len < n:
        curr_len *= 2
        operations += 1
    operations += n - curr_len // 2
    return operations
