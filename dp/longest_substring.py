#!/usr/bin/env python

"""
Find the length of the smallest substring with maximum number of distinct characters

"""

def _initialize_char_indices():
    char_idx = [-1] * 256
    return char_idx


def longest_substring(str):
    # this array will be used to store the last index of the char in
    # the original string
    char_idx = _initialize_char_indices()
    char_idx[ord(str[0])] = 0 #

    # The max substring will be calculated using start_idx + max_length
    # so we shall modify them accordingly
    max_length = 1 # Global max length
    start_idx = 0  # Global start index
    curr_length = 1 # length of the sliding window
    prev_idx = 0

    for i in range(1, len(str)):
        prev_idx = char_idx[ord(str[i])]
        # new character encountered for the first time or beyond the sliding window
        if prev_idx == -1 or i - curr_length > prev_idx:
            curr_length += 1
        else:
            if curr_length > max_length:
                max_length = curr_length
                start_idx = i - max_length
            curr_length = i - prev_idx
        char_idx[ord(str[i])] = i

    if curr_length > max_length:
        max_length = curr_length
        start_idx = len(str) - max_length

    return str[start_idx:start_idx + max_length]


if __name__ == '__main__':
    l = "abacdabcdefgh"
    print longest_substring(l)