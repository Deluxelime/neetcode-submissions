class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listS = list(s)
        listT = list(t)
        list.sort(listS)
        list.sort(listT)

        if listS == listT:
            return True

        return False
        