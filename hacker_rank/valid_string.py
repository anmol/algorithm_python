#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
"""
from collections import defaultdict
import sys


def is_valid(s):
    if len(s) == 1:
        return 'YES'
    freq_chars = defaultdict(int)
    for i in range(len(s)):
        freq_chars[s[i]] += 1
    print(freq_chars)
    freq_freq = defaultdict(int)
    for val in freq_chars.values():
        freq_freq[val] += 1
    print(freq_freq)
    if len(freq_freq) == 1:
        return 'YES'
    elif len(freq_freq) == 2:
        # one of key values should be 1
        # the one which is 1 should have key ==1 or > other key
        # and greater - smaller = 1
        key_list = list(freq_freq.keys())
        k1, v1 = key_list[0], freq_freq[key_list[0]]
        k2, v2 = key_list[1], freq_freq[key_list[1]]
        if v1 == 1:  # and abs(k1 - k2) == 1:
            if (k1 > k2 and abs(k1 - k2) == 1) or k1 == 1:
                return 'YES'
            else:
                return 'NO'
        elif v2 == 1:  # and abs(k1 - k2) == 1:
            if (k2 > k1 and abs(k1 - k2) == 1) or k2 == 1:
                return 'YES'
            else:
                return 'NO'
        else:
            return 'NO'
    else:
        return 'NO'


if __name__ == '__main__':
    # print("python version: " + sys.version)
    s = "ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghad" \
    "hdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiie" \
    "dcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicb" \
    "gigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeei" \
    "bgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffe" \
    "bdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhif" \
    "hgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabe" \
    "iaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadf" \
    "ihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifd" \
    "cbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiff" \
    "chbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdi" \
    "abcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcich" \
    "adgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfd" \
    "hhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbe" \
    "cgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaa" \
    "dedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgeh" \
    "iidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd"

    # s = "aaaabbcc"
    s = "aaaabb"

    print(is_valid(s))
