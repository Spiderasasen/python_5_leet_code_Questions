from typing import Optional

import Reading_text_files as reading

def read_question() -> None:
    reading.read_text_file('Text_Files_for_Questions/add_2_numbers.txt')


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def longestPalindrome(self, s: str) -> str:
        repeating_words = ''



        return repeating_words


def solutions() -> None:
    print(Solution().longestPalindrome('babad'))
    print(Solution().longestPalindrome('cbba'))
    print(Solution().longestPalindrome('cba'))