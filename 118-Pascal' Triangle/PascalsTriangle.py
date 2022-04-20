def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print(':', actual == expect)

test0 = {'Input': 
                 {'numRows': 5
                  },
         'Output': [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
         }

test1 = {'Input': 
                 {'numRows': 1
                  },
         'Output': [[1]]
         }

test2 = {'Input': 
                 {'numRows': 2
                  },
         'Output': [[1],[1,1]]
         }

tests = [test0, test1, test2]

#%% My solution - dynamic programming
def generate(numRows: int) -> list:
    table = [ [0 for _ in range(i+2)] for i in range(numRows+2) ]
    List = []
    table[0][0] = 1
    for idx1 in range(numRows+1):
        for idx2 in range(idx1+1):
            # print('idx1:', idx1, 'idx2', idx2)
            table[idx1+1][idx2+1] = table[idx1][idx2] + table[idx1][idx2+1]
        List.append(table[idx1+1][1:-1])
    return List[:-1]

evaluate(generate, tests)

#%% Inspired by Discussion - better dynamic programming - iterative
# Time O(n*n) Space O(n*n)
def generate2(numRows: int) -> list:
    res = [[1]*(i+1) for i in range(numRows)] # initialize list of lists with 1s
    for i in range(2, numRows):
        for j in range(1, i):
            res[i][j] = res[i-1][j-1] + res[i-1][j]
    return res

#%% Inspired by Discussion - Top-down recursive
# Time O(n*n) Space O(n*n)
def generate3(n: int) -> list:
    def helper(n):
        if n:
            helper(n-1)                 # generate above row first
            ans.append([1]*n)           # insert current row into triangle
            for i in range(1, n-1):     # update current row values using above row
                ans[n-1][i] = ans[n-2][i] + ans[n-2][i-1]
    ans = []
    helper(n)
    return ans
