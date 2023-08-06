# digits/solver/operations.py

from itertools import combinations
from solver.strategy import Strategy

def brute_force_solutions(target, numbers, path, memo):
    numbers = sorted(numbers, reverse=True)
    combos = nc2(numbers)
    valid_paths = []

    for a, b, rest in combos:
        operations = [
            {'result': a * b, 'valid': a > 1 and b > 1, 'path': path + [f"{a} * {b}"]},
            {'result': a + b, 'valid': True, 'path': path + [f"{a} + {b}"]},
            {'result': a - b, 'valid': a - b > 0 and a - b != b, 'path': path + [f"{a} - {b}"]},
            {'result': a / b, 'valid': a % b == 0 and b != 1, 'path': path + [f"{a} / {b}"]},
        ]

        for op in operations:
            if op['valid'] and op['result'] == target:
                valid_paths.append(op['path'])
                return valid_paths

            if op['valid']:
                rest_clone = rest[:]
                rest_clone.append(op['result'])
                key = tuple(sorted(rest_clone))
                if key in memo:
                    valid_paths.extend(memo[key])
                else:
                    result = brute_force_solutions(target, rest_clone, op['path'], memo)
                    memo[key] = result
                    valid_paths.extend(result)

    return valid_paths

def nc2(numbers):
    res = []
    for comb in combinations(numbers, 2):
        a, b = comb
        rest = [num for num in numbers if num != a and num != b]
        res.append((a, b, rest))
    return res

def operations(target, numbers, strategy):
    memo = {}
    solutions = brute_force_solutions(target, numbers, [], memo)
    if strategy == Strategy.SHORTEST:
        return sorted(solutions, key=len)[0]
    elif strategy == Strategy.LONGEST:
        return sorted(solutions, key=len, reverse=True)[0]
