from collections import defaultdict
class Solution:
    def mostCommonWord(self, para: str, ban: List[str]) -> str:
        punc = "!?',;."
        for char in punc:
            para = para.replace(char, " ")
        words = para.lower().split(' ')
        d = defaultdict(int)
        for word in words:
            if word:
                d[word] += 1
        maxx = -1
        ans = ""
        for i in d:
            if i not in ban:
                maxx = max(maxx, d[i])
                if d[i] == maxx:
                    ans = i
        for word, count in d.items():
            print(f"{word}: {count}")
        return ans

