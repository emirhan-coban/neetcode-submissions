class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        for num in nums:
            if num not in groups:
                groups[num] = 1
            else:
                groups[num] = groups[num] + 1
        topFreqs = sorted(groups.items(), key=lambda x: x[1], reverse=True)

        answer = [x[0] for x in topFreqs[:k]]
        return answer

