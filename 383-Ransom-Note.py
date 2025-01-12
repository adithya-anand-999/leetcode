class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for c in ransomNote:
            try:
                magazine[magazine.index(c)] = '*'
            except ValueError:
                return False
        return True