class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        max_active = sum([1 for char in s if char == '1'])
        groups = []
        new_s = '1' + s + '1'
        current = '1'
        count = 0

        for i in range(1, len(new_s)):
            if new_s[i] != current:
                groups.append((count, current))
                current = new_s[i]
                count = 1
            else:
                count += 1

        groups.append((count, current))
        max_group = 0

        for i in range(2, len(groups)):
            if groups[i - 2][1] == '0' and groups[i][1] == '0':
                max_group = max(max_group, groups[i - 2][0] + groups[i][0])

        return max(max_active, max_active + max_group)