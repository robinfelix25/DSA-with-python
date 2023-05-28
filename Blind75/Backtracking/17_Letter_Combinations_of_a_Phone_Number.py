
'''
I was asked a similar question in Google.
'''
def letterCombinations(digits):
        res = []
        map = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        def backtrack(i, cur):
            if len(cur) == len(digits):
                res.append(cur)
                return

            for c in map[digits[i]]:
                backtrack(i+1, cur + c)
        
        if digits:
            backtrack(0,"")

        return res

digits = "23"      
print(letterCombinations(digits))