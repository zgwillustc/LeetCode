def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print(':', actual == expect)

test0 = {'Input':
                 {'nums1': [1,2,2,1],
                  'nums2': [2,2]
                  },
         'Output': [2,2]
         }

test1 = {'Input':
                 {'nums1': [4,9,5],
                  'nums2': [9,4,9,8,4]
                  },
         'Output': [4,9]
         }

test2 = {'Input':
                 {'nums1': [3,6],
                  'nums2': [2,1]
                  },
         'Output': []
         }

tests = [test0, test1, test2]

#%% My solution
def intersect(nums1, nums2):
    pass

evaluate(intersect, tests)
