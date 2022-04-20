test0 = {'Input': 
                 {'s': 'III'
                  },
         'Output': 3
         }

test1 = {'Input': 
                 {'s': 'LVIII'
                  },
         'Output': 58
         }

test2 = {'Input': 
                 {'s': 'MCMXCIV'
                  },
         'Output': 1994
         }

tests = [test0, test1, test2]
    
trans2 = {'I': 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000,
         'IV': 5,
         'IX': 10,
         'XL': 40,
         'XC': 90,
         'CD': 400,
         'CM': 900
         }

trans = {'I': 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000}

# If the next symbol is larger than the current symbol, substract twice of it,
# Otherwise, add it
def romanToInt(s: str) -> int:
    total = trans[s[0]]
    n = len(s)
    for i in range(1, n):
        if trans[s[i]] > trans[s[i-1]]:
            total += trans[s[i]] - 2 * trans[s[i-1]]
        else:
            total += trans[s[i]]
    return total

# Inspired by the hint.
# Start from the right of the string to the left
def romanToInt2(s: str) -> int:
    total = 0 
    prev = 0
    for char in reversed(s): # s[::-1] creates a list while reversed creates a generator
        curr = trans[char]
        if curr < prev:
            total -= curr
        else:
            total += curr
        prev = curr
    return total

# An interesting solution
def romanToInt3(s: str) -> int:
    s = s.replace('IV', 'IIII').replace('IX', 'VIIII')
    s = s.replace('XL', 'XXXX').replace('XC', 'LXXXX')
    s = s.replace('CD', 'CCCC').replace('CM', 'DCCCC')
    total = 0
    for char in s:
        total += trans[char]
    return total


