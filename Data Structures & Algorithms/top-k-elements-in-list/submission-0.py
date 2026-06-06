class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count =Counter(nums)
        sortedele=sorted(count.keys(),key=count.get,reverse=True)
        return sortedele[:k]