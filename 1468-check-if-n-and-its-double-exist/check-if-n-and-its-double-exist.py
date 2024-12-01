class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = set()
        for x in arr:
            if 2*x in d or (x%2==0 and x//2 in d):
                return True
            d.add(x)
        return False