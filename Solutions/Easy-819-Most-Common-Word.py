"""
    819. Most Common Word
    https://leetcode.com/problems/most-common-word/
"""


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:

        paragraph = "".join(
            char.lower() if char.isalnum() else " " for char in paragraph
        )  # check each char if alphanumeric, if not replace with space
        banned = set(banned)  # creating set of banned words to reduce lookup time
        word_dict = {}

        max_word_counter = 0
        max_word = ""

        for word in paragraph.split():  # words are split by space
            if word not in banned:
                word_dict[word] = (
                    word_dict.get(word, 0) + 1
                )  # get count of word if exists, else default value 0

                if (
                    word_dict[word] > max_word_counter
                ):  # max_counter and related word updating
                    max_word_counter = word_dict[word]
                    max_word = word

        return max_word


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(f"paragraph: {paragraph} \nbanned: {banned} \noutput: {Solution().mostCommonWord(
        paragraph=paragraph,
        banned=banned,
    )} \n")

paragraph = "a."
banned = []
print(f"paragraph: {paragraph} \nbanned: {banned} \noutput: {Solution().mostCommonWord(
        paragraph=paragraph,
        banned=banned,
    )} \n")

paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]
print(f"paragraph: {paragraph} \nbanned: {banned} \noutput: {Solution().mostCommonWord(
        paragraph=paragraph,
        banned=banned,
    )} \n")
