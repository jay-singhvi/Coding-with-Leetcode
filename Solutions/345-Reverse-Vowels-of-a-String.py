"""
    345. Reverse Vowels of a String
    https://leetcode.com/problems/reverse-vowels-of-a-string/
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """

        # Convert the string to list for easier manipulation
        s = list(s)
        print(f"Converted string '{s}' to list '{s}'")

        # Create a list to store vowels
        vowel_list = []

        # Iterate through each character in the list
        for i in range(len(s)):
            # If it is a vowel, add it to the vowel list and replace it with "_"
            if s[i].lower() in ("a","e","i","o","u"):
                print(f"Character '{s[i]}' is a vowel, added to vowel list '{vowel_list}' and replaced with '_'")
                vowel_list.append(s[i])
                s[i] = "_"

        # Iterate through each character in the list again
        for i in range(len(s)):
            # If it is "_", replace it with the last vowel from the vowel list
            if s[i] in ("_"):
                print(f"Character '_' replaced with vowel '{s[i]}' from vowel list '{vowel_list}'")
                s[i] = vowel_list.pop()

        # Join the list back into a string and return it
        print(f"Reversed vowels in string '{s}'")
        return "".join(s)
