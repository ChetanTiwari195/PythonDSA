
from typing import List


def partition(s: str) -> List[List[str]]:
    res = []

        # Helper to check if a string is a palindrome
    def is_palindrome(string):
        return string == string[::-1]

        # Backtracking function
    def backtrack(start, path):
            # If we've reached the end of the string, add the current path
        if start == len(s):
            res.append(path[:])  # Make a copy of current path
            return

            # Try all possible cuts from start to end
        for end in range(start, len(s)):
            substring = s[start:end+1]
            if is_palindrome(substring):
                path.append(substring)              # Choose
                backtrack(end + 1, path)            # Explore
                path.pop()                          # Un-choose (backtrack)

    backtrack(0, [])
    print(res)



partition("aab")