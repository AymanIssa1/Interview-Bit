class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, text):
        filtered_text = "".join(c for c in text.lower() if c.isalnum())
        if filtered_text == filtered_text[::-1]:
            return 1
        return 0


print(Solution.isPalindrome('', "A man, a plan, a canal: Panama"))
print(Solution.isPalindrome('', "race a car"))
