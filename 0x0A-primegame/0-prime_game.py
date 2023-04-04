#!/usr/bin/python3
"""prime game"""


def isWinner(x, nums):
    """winner function"""
    def get_primes(n):
        """fucntion to get primes"""
        sieve = [True] * (n+1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5)+1):
            if sieve[i]:
                for j in range(i*i, n+1, i):
                    sieve[j] = False
        return [i for i in range(n+1) if sieve[i]]

    def play_game(n):
        """handles game play"""
        primes = get_primes(n)
        player = 0
        remaining = set(range(1, n+1))
        while primes:
            p = primes.pop(0)
            multiples = set(range(p, n+1, p))
            remaining -= multiples
            if not remaining:
                return player
            player = 1 - player
        return 1 - player

    scores = [0, 0]
    for n in nums:
        winner = play_game(n)
        scores[winner] += 1
    if scores[0] == scores[1]:
        return None
    else:
        return "Maria" if scores[0] > scores[1] else "Ben"
