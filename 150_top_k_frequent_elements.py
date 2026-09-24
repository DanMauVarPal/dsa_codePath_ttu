class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1
        
        counter = sorted(numHash, key=numHash.get())

        bucket = [[] for i in range(len(nums)+1)]

        for num, freq in counter.items():
            bucket[freq].append(num)

        out = []
        for i in range(1, len(nums)+1)
            out.extend(nums[-i])

        return out[0:k]
