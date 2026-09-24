class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        def getChars(word):
            hash = [0]*26

            for ch in word:
                hash[ord(ch) - ord('a')] += 1

            return hash
        
        for word in strs:
            hs = getChars(word)
            anagrams[hs].append(word)
        
        return list(anagrams.values())