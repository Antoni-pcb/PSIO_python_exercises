from typing import List

def fib(n: int) -> List[int]:
    result = []
    a, b = 0, 1
    for i in range(n):
        result.append(b)
        a, b = b, a + b
    return result