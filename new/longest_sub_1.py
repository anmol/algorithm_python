import os
# longest substring without repeating characters


def longest_sub(s: str):
    l = []
    for i in range(len(s)):
        d = {}
        for j in range(i, len(s)):
            if s[j] in d:
                break
            d[s[j]] = 1
        if len(d) > len(l):
            l = s[i:j]
    return l

def longest_sub_2(s: str):
    d = {}
    l = []
    i = j = 0
    while i < len(s) and j < len(s):
        if s[j] in d:
            i = d[s[j]] + 1
            del d[s[j]]
        d[s[j]] = j    
        j += 1
        l = s[i:j] if len(s[i:j]) > len(l) else l
        print(l)
    print("-----end-loop-----")
    return l


if __name__ == "__main__":
    print(longest_sub("abcabcbb"))
    print(longest_sub_2("abcabcbb"))