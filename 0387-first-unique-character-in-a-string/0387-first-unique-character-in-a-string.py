class Solution:
    def firstUniqChar(self, s):
         # Create a list to store the frequency of each character
        frequency = [0] * 26  # Assuming only lowercase letters

        # Step 1: Count the frequency of each character
        for char in s:
            frequency[ord(char) - ord('a')] += 1  # Map 'a' to 0, 'b' to 1, ..., 'z' to 25

        # Step 2: Find the first character with a frequency of 1
        for index, char in enumerate(s):
            if frequency[ord(char) - ord('a')] == 1:
                return index  # Return the index of the first unique character

        # Step 3: If no unique character is found, return -1
        return -1