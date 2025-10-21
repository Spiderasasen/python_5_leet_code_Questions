import Reading_text_files as reading

class Longest_Palindrome:
    def question(self):
        reading.read_text_file('Text_Files_for_Questions/add_2_numbers.txt')

    def code(self):
        reading.read_text_file('Code_Text_files/Longest_Palindrom.txt')

    def solution(self) -> None:
        solutions()

class Solution:
    def longestPalindrome(self, s: str) -> str:
        #if nothing is in the code, just return nothing
        if not s or len(s) == 0:
            return ''

        st: str = s.lower()

        longest_palindrome = ''

        #palindrome function for the code
        def exanding_around(left, right):
            while left >= 0 and right < len(st) and st[left] == st[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s)):
            palindrome1: str = exanding_around(i, i) #odd
            palindrome2: str = exanding_around(i, 1 + i) #even

            #updating the longest palindrome if needed
            if len(palindrome1) > len(longest_palindrome):
                longest_palindrome = palindrome1
            if len(palindrome2) > len(longest_palindrome):
                longest_palindrome = palindrome2

        return longest_palindrome

def solutions() -> None:
    print(Solution().longestPalindrome('babad'))
    print(Solution().longestPalindrome('cbba'))
    print(Solution().longestPalindrome('cba'))
    print(Solution().longestPalindrome('abba'))
    print(Solution().longestPalindrome(''))
    print(Solution().longestPalindrome('texas'))
    print(Solution().longestPalindrome('alaska'))
    print(Solution().longestPalindrome('Alaska'))