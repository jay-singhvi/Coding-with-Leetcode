"""
    937. Reorder Data in Log Files
    https://leetcode.com/problems/reorder-data-in-log-files/
"""


class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letter_log = []
        digit_log = []

        for log in logs:
            if log.split()[1].isdigit():  # check if 2nd word is a digit or not
                digit_log.append(log)  # if digit add log as is to list
            else:
                letter_log.append(
                    log.split()
                )  # if string add log after splitting to a list

        letter_log.sort()  # sort string list by identifier as its the 1st record in each log
        letter_log.sort(
            key=lambda x: x[1:]
        )  # sort string by logs of string - all except identifier

        for i in range(len(letter_log)):
            letter_log[i] = " ".join(letter_log[i])  # join all words of the log

        letter_log.extend(digit_log)  # completed log

        return letter_log


print(
    Solution().reorderLogFiles(
        [
            "dig1 8 1 5 1",
            "let1 art can",
            "dig2 3 6",
            "let2 own kit dig",
            "let3 art zero",
        ]
    )
)
print(
    Solution().reorderLogFiles(
        ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    )
)
