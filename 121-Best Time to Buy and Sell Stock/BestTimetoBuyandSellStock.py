def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print(':', actual == expect)

test0 = {'Input':
                 {'prices': [7,1,5,3,6,4]
                  },
         'Output': 5
         }

test1 = {'Input':
                 {'prices': [7,6,4,3,1]
                  },
         'Output': 0
         }

test2 = {'Input':
                 {'prices': [3]
                  },
         'Output': 0
         }

tests = [test0, test1, test2]

#%% My solution - brute force - exceeds time limit
# Time O(n * n) Space O(1)
def maxProfit(prices) -> int:
    profit, length = 0, len(prices)
    for left in range(length):
        for right in range(left+1, length):
            if prices[right] - prices[left] > profit:
                profit = prices[right] - prices[left]
    return profit

#    # Official solution - but still exceeds time limit
#    max_profit = 0
#    for i in range(len(prices) - 1):
#        for j in range(i + 1, len(prices)):
#            profit = prices[j] - prices[i]
#            if profit > max_profit:
#                max_profit = profit
#
#    return max_profit

evaluate(maxProfit, tests)

#%% My solution - max() - exceeds time limit
def maxProfit(prices) -> int:
    profit, length = 0, len(prices)
    for left in range(length):
        future_max = max(prices[left:])
        if future_max - prices[left] > profit:
            profit = future_max - prices[left]
    return profit

evaluate(maxProfit, tests)

#%% One pass - Official solution
# Time O(n) Space O(1)
def maxProfit(prices) -> int:
    min_price = float('inf') # "A very large number"
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    return max_profit
evaluate(maxProfit, tests)

#%% Min so far
def maxProfit(prices) -> int:
    max_profit = 0
    min_price = prices[0]
    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    return result
evaluate(maxProfit, tests)

#%% Kadane's Algorithm
def maxProfit(prices) -> int:
    n = len(prices)
    ans = 0
    curSum = 0
    for i in range(n-1):
        curSum += prices[i+1] - prices[i]
        if curSum < 0:
            curSum = 0
        ans = max(ans, curSum)
    return ans
