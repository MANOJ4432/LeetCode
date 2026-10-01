class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        if target[0] == source[0] and target[1] == source[1]:
            return 0
        if target[0] == source[0] or target[1] == source[1] or target[0]-target[1] == source[0]-source[1] or target[0]+target[1] == source[0]+source[1]:
            return 1
        return 2
            