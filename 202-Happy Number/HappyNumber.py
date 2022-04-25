# Inspired by the Solution
class Solution:
# Approach 1: Detect Cycles with a HashSet
# Time O(log n) Space O(log n)
# There are 2 parts to the algorithm we'll need to design and code.
# 1. Given a number nn, what is its next number?
# 2. Follow a chain of numbers and detect if we've entered a cycle.
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                digit = n % 10
                n = n // 10
                total_sum += digit**2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1

# Approach 2: Floyd's Cycle-Finding Algorithm
# Time O(log n) Space O(1)
# The chain we get by repeatedly calling getNext(n) is an implicit LinkedList
    def isHappy2(self, n: int) -> bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1

# Approach 3: Hardcoding the Only Cycle
# Time O(log n) Space O(1)
# there's only one cycle: 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4.
# All other numbers are on chains that lead into this cycle, or on chains that lead into 11.
    def isHappy3(self, n: int) -> bool:
        cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}

        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        while n != 1 and n not in cycle_members:
            n = get_next(n)

        return n == 1

# Inspired by the Discussion
    def isHappy4(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(x) **2 for x in str(n)])
        return n == 1


def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print(':', actual == expect)

test0 = {'Input':
                 {'n': 19
                  },
         'Output': True
         }
test1 = {'Input':
                 {'n': 2
                  },
         'Output': False
         }
test2 = {'Input':
                 {'n': 1
                  },
         'Output': True
         }
tests = [test0, test1, test2]

def main():
    solution = Solution()
    evaluate(solution.isHappy, tests)

if __name__ == '__main__':
    main()
