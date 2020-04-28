#!/usr/bin/python3
"""
input: 3[a2[b]]
output: abbabbabb
"""


def decode(a):
    n = len(a)
    int_stack = []
    char_stack = []
    for i in range(n):
        if a[i].isdigit():
            int_stack.append(int(a[i]))
        if a[i].isalpha() or a[i] == '[':
            char_stack.append(a[i])
        if a[i] == ']':
            temp_str = ''
            while True:
                popped = char_stack.pop()
                if popped != '[':
                    temp_str = popped + temp_str
                else:
                    break
            it = int_stack.pop()
            temp_str = temp_str * it
            char_stack.append(temp_str)
    final_str = ''
    while len(char_stack) != 0:
        final_str = char_stack.pop() + final_str
    return final_str


if __name__ == '__main__':
    print(decode("3[a2[b]]"))