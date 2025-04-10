from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count frequencies
        freq = Counter(words)
        
        # Sort by frequency desc, then lexicographically
        sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        
        # Return top k words
        return [word for word, count in sorted_words[:k]]
