class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # saves a lot of time with long strings
        if len(s) != len(t):
            return False

        letter_map = {}

        for letter in s:
            if letter not in letter_map:
                letter_map[letter] = 1
            else:
                letter_map[letter] += 1

        for letter in t:
            if letter not in letter_map:
                return False
            else:
                letter_map[letter] -= 1
                if letter_map[letter] < 0:
                    return False

        return True