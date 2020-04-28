import os


def matching_bracket(c):
    if c == '}':
        return '{'
    if c == ')':
        return '('
    if c == ']':
        return '['


def is_balanced(s):
    char_stack = []
    for i in range(len(s)):
        if s[i] in ('{', '[', '('):
            char_stack.append(s[i])
        elif len(char_stack) == 0 or char_stack.pop() != matching_bracket(s[i]):
            return 'NO'
        else:
            continue
    if len(char_stack) == 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    # print(is_balanced('{[(])}')
    # print(is_balanced('{{[[(())]]}}'))

    # fptr = open(os.environ['INPUT_PATH'] + '/test.txt', 'r')
    # fptrw = open(os.environ['OUTPUT_PATH'] + '/test.txt', 'w')

    fptr = open(os.environ['INPUT_PATH'] + '/balanced_bracket_input.txt', 'r')
    fptrw = open(os.environ['OUTPUT_PATH'] + '/balanced_bracket_output.txt', 'w')

    # t = int(input())
    _ = fptr.readline()
    lines = fptr.readlines()
    for line in lines:
        # fptrw.write(line)
        # for t_itr in range(t):
        # s = input()
        result = is_balanced(line.strip())
        fptrw.write(result + '\n')

    fptr.close()
    fptrw.close()
