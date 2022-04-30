class Solution:
    # Exceed time limit - should use dynamic programming.
    def coinChange(self, coins: list, amount: int) -> int:
        if amount == 0:
            return 0

        def recursion(coins, amount):
            best = None
            for idx, coin in enumerate(coins):
                remainder = amount - coin
                if remainder < 0:
                    continue
                elif remainder == 0:
                    current = [coin]
                else:
                    current = recursion(coins[idx:], remainder)
                    if current:
                        current.append(coin)
                    else:
                        continue

                if best:
                    if len(best) > len(current):
                        best = current
                else:
                    best = current
            return best

        result = recursion(coins, amount)
        return len(result) if result else -1


def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Actual:', actual)
        print(':', actual == expect)

test0 = {'Input':
                 {'coins': [1, 2, 5],
                  'amount': 11
                  },
         'Output': 3
         }

test1 = {'Input':
                 {'coins': [2],
                  'amount': 3
                  },
         'Output': -1
         }

test2 = {'Input':
                 {'coins': [1],
                  'amount': 0
                  },
         'Output': 0
         }

tests = [test0, test1, test2]

def main():
    solution = Solution()
    evaluate(solution.coinChange, tests)

if __name__ == '__main__':
    main()
