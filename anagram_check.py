# Check two strings for anagram

from collections import Counter

str_1, str_2, str_3 = "acbde", "aadcb", "abcda"
cnt_1, cnt_2, cnt_3  = Counter(str_1), Counter(str_2), Counter(str_3)

if cnt_1 == cnt_2:
    print('1 and 2 anagram')
if cnt_1 == cnt_3:
    print('1 and 3 anagram')
if cnt_2 == cnt_3:
    print('2 and 3 anagram')
