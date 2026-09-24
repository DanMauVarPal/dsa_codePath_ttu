class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def hash_word(word):
            # hash = {}
            # 
            # for ch in word:
            #     hash[ch] = hash.get(ch, 0) + 1 # Gets character value on hash or initializes at 0
            # 
            # return hash

            hash = defaultdict(int)

            for ch in word:
                hash[ch] += 1

            return hash
        
        return hash_word(s) == hash_word(t)