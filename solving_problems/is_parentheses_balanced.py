"""
Check for balanced parentheses in Python
Given an expression string, write a python program to find whether a given string has balanced parentheses or not.

Examples:

Input : {[]{()}}
Output : Balanced

Input : [{}{}(]
Output : Unbalanced

"""

# Approach #1 : Using stack
"""
One approach to check balanced parentheses is to use stack. Each time, when an open parenthesis
is encountered push it in the stack, and when closed one is encountered,
match it with the top of stack and pop it. If stack is empty at the end,
return Balanced otherwise, Unbalanced.
"""

# Python3 code to Check for
# balanced parentheses in an expression
opening_list = ["[", "{", "("]
# mirorred parantheses at the same order as in the opening list
closing_list = ["]", "}", ")"]

# Function to check parentheses


def check_stack(myStr):
    stack = []
    for paren in myStr:
        if paren in opening_list:
            stack.append(paren)
        elif paren in closing_list:
            # find the current parenthesis index in the closing list
            index = closing_list.index(paren)
            topmost = len(stack)-1
            if ((len(stack) > 0) and
                    (opening_list[index] == stack[topmost])):
                stack.pop()
                # if the parantheses in the opening list, at the same position as we define for the paranthesis
                # in the closing list, equal to the topmost paranthesis in the stack, we consider it as
                # corresponding to the opened one and pop up from the stack
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


# Driver code
string = "{[]{()}}"
print(string, "-", check_stack(string))

string = "[{}{})(]"
print(string, "-", check_stack(string))

string = "((()"
print(string, "-", check_stack(string))

string = ""
print(string, "-", check_stack(string))


# Approach #2 : Using queue

"""First Map opening parentheses to respective closing parentheses.
Iterate through the given expression using ‘i’, if ‘i’ is an open parentheses,
append in queue, if ‘i’ is close parentheses, Check whether queue is empty or ‘i’
is the top element of queue, if yes, return “Unbalanced”, otherwise “Balanced”"""
# Python3 code to Check for
# balanced parentheses in an expression


def check_queue(expression):

    open_tup = tuple('({[')
    close_tup = tuple(')}]')
    map = dict(zip(open_tup, close_tup))
    queue = []

    for paren in expression:
        if paren in open_tup:
            queue.append(map[paren])
            """bcs of the zip function, we append to the queue a closing parenthesis,
            which is a value (in a map key-value pair) for the key, represented by
            the opening parenthesis"""
        elif paren in close_tup:
            if not queue or paren != queue.pop():
                # if the parenthesis in the closing tuple is not the same which is popped from the queue,
                # then it is not a balanced string of parantheses
                return "Unbalanced"
    if not queue:
        return "Balanced"
    else:
        return "Unbalanced"


# Driver code
string = "{[]{()}}"
print(string, "-", check_queue(string))

string = "((()"
print(string, "-", check_queue(string))


# Approach#3 : Elimination based
"""In every iteration, the innermost brackets get eliminated (replaced with empty string).
If we end up with an empty string, our initial one was balanced; otherwise, not."""

# Python3 code to Check for
# balanced parentheses in an expression


def check_by_elimination(my_string):
    brackets = ['()', '{}', '[]']
    while any(x in my_string for x in brackets):
        # same as: for x in brackets:
        #   if(x in my_string):
        # or
        # while parentheses from the brackets list are found in the string passed as an argument to the function
        for br in brackets:
            # iterate through the parentheses in the brackets list
            my_string = my_string.replace(br, '')
            # and replace the current pair of parentheses with the empty string
    # return inverted result (when it is empty string, falsy inversed to truthy,
    # then the parantheses were balanced; and vice versa)
    return not my_string


# Driver code
string = "{[]{()}}"
print(string, "-", "Balanced"
      if check_by_elimination(string) else "Unbalanced")
