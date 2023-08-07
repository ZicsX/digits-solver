import operator
import numpy as np
from solver.strategy import Strategy
from solver.operations import operations


# Four basic arithmetic operations
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '//': operator.floordiv
}

def generate_numbers(index):
    number_ranges = [(1, 10), (1, 10), (1, 12), (1, 12), (1, 12)]
    range_lengths = [(5, 1), (5, 1), (4, 2), (4, 2), (3, 3)]
    expr_seq = [4,4,5,5,6]
    targets_range = [(56, 98), (111, 197), (223, 292), (335, 386), (400, 479)]

    numbers = np.random.choice(np.arange(*number_ranges[index]), range_lengths[index][0], replace=False)
    numbers = np.concatenate([numbers, np.random.choice(np.arange(12, 26), range_lengths[index][1], replace=False)])

    return np.sort(numbers), np.sort(np.random.choice(numbers, expr_seq[index], replace=False)), targets_range[index]

def get_puzzle(ps, max_attempts=1000):
    def generate_target(ps):
        numbers,nums,target_range  = generate_numbers(ps)

        random_nums = np.random.choice(nums, len(nums), replace=False)

        expr = str(random_nums[0])
        val = random_nums[0]

        for num in random_nums[1:]:
            op = np.random.choice(list(ops.keys()))

            if op == '//' and num == 0:
                continue

            val = ops[op](val, num)

            if op in ['+', '-']:
                expr = '({} {} {})'.format(expr, op, num)
            else:
                expr = '{} {} {}'.format(expr, op, num)

        if target_range[0] <= val <= target_range[1]:
            return val, expr, np.sort(numbers)

        return None, None, None
    
    for _ in range(max_attempts):
        target, expr, nums = generate_target(ps)
        if target is not None:
            print('Numbers:', nums)
            print('Target:', target)
            print('Expression:', expr)
            print('Hint:',operations(target, nums,Strategy.SHORTEST))
            break
    else:
        print("Failed to generate a puzzle after", max_attempts, "attempts.")

get_puzzle(0)
