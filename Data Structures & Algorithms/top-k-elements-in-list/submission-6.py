class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1

        keyMax = []
        keyHash = set()

        for _ in range(k):
            maxValue = -1000
            maxCount = 0

            for key, value in hashMap.items():
                if value > maxCount and key not in keyHash:
                    maxValue = key
                    maxCount = value
            
            keyMax.append(maxValue)
            keyHash.add(maxValue)
        
        return keyMax
                
            