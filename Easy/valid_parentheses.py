# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# "Aberturas"      "Fechamento"
#       ( [ {       } ] )

s = "([{}])"


class Solution:
    def isValid(self, s: str) -> bool:
        pile_open_brackets = []
        except_brackets = { "(" : ")", "[" : "]", "{" : "}" }
        
        for char in s:
            if char in except_brackets:
                # char é um caractere de abertura
                pile_open_brackets.append(char)
            elif char in except_brackets.values():
                # char é um caractere de fechamento
                if pile_open_brackets:
                    last_open_char = pile_open_brackets.pop()
                else:
                    return False
                expected_closing = except_brackets[last_open_char]
                if expected_closing != char:
                    return False
            else:
                return False
        if pile_open_brackets:
            return False
        
        return True


solution = Solution()

print(solution.isValid(s))
