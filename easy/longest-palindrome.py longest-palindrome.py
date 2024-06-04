# 409. Longest Palindrome
# Solved
# Easy
# Topics
# Companies
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
# palindrome
#  that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome.
#
#
#
# Example 1:
#
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:
#
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
#
#
# Constraints:
#
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.

def longestPalindrome(self, s: str) -> int:
        freq= {}
        longestPalindrome = 0 
        oddValue = 0
        for x in s : 
            if x in freq: 
                freq[x] += 1
            else:
                freq[x] = 1
        for f in freq.values():
            if f % 2 == 0 :
                # Even Frequency 
                longestPalindrome += f
            else:
                # Odd Condition 
                longestPalindrome += f -1 
                oddValue =1 
        return  longestPalindrome + oddValue

print(longestPalindrome("aabbb"))
