class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap={}
        
        for s in strs:
            arr = [0] * 26
            for ch in s:
                arr[ord(ch) - ord('a')] += 1

            key = tuple(arr)

            if key not in hashMap:
                hashMap[key] = []
                
            hashMap[key].append(s)
            
        return list(hashMap.values())