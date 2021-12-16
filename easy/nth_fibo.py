# Time O(2^n), Space O(n)
def getNthFib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n-2) + getNthFib(n-1)

# Dynamic programming approach


def getNthFibDynamic(n, memo={1: 0, 2: 1}):
    if n in memo:
        return memo[n]
    else:
        memo[n] = getNthFibDynamic(n-2, memo) + getNthFibDynamic(n-1, memo)
        return memo[n]


print(getNthFibDynamic(35))
print(getNthFib(35))
