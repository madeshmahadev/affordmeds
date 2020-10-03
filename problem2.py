#Problem 2:
#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input
#string is valid. An input string is valid if –
#• Open brackets must be closed by the same type of brackets.
#• Open brackets must be closed in the correct order.


class Problem2:
    def check_valid(string):
        brackets = {"(": ")", "{": "}", "[": "]"} #Parentheses Allowed
        stack = list() #Initializing Stack
        for bracket in string:
            if bracket in brackets:
                stack.append(bracket)
            elif len(stack) == 0 or brackets[stack.pop()] != bracket:
                return False
        return len(stack)==0 #Clearing Stack

if __name__=="__main__":
    #Test Case1
    testcase1 = Problem2.check_valid('()')
    print(testcase1)
    #Test Case2
    testcase2 = Problem2.check_valid('()[]{}')
    print(testcase2)
    #Test Case3
    testcase3 = Problem2.check_valid('{]')
    print(testcase3)
    #Test Case4
    testcase4 = Problem2.check_valid('([)]')
    print(testcase4)
    #Test Case5
    testcase5 = Problem2.check_valid('{[]}')
    print(testcase5)
