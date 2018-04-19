# Triple step


def triple_step(n, memo={}):
    if n < 0: return 0
    if n == 0: return 1
    if n in memo: return memo[n]

    memo[n] = triple_step(n-1) + triple_step(n-2) + triple_step(n-3)

    return memo[n]


if __name__ == "__main__":
    print triple_step(1)
    print triple_step(2)
    print triple_step(3)
    print triple_step(4)
    print triple_step(5)
