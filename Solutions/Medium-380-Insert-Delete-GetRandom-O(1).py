"""
    380. Insert Delete GetRandom O(1)
    https://leetcode.com/problems/insert-delete-getrandom-o1/
"""

import random


class RandomizedSet:
    def __init__(self):
        self.result_set = set()

    def insert(self, val: int) -> bool:
        if val not in self.result_set:
            self.result_set.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.result_set:
            self.result_set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.result_set))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
