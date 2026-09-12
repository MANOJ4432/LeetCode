class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        i=0
        j=1
        while j<len(intervals):
            if intervals[j][0] in list(range(intervals[i][0],intervals[i][1]+1)) and  intervals[j][1] in list(range(intervals[i][0],intervals[i][1]+1)):
                intervals.remove(intervals[j])
            elif intervals[j][0] in list(range(intervals[i][0],intervals[i][1]+1)):
                intervals[i][1]=intervals[j][1]
                intervals.remove(intervals[j])
            else:
                j+=1
                i+=1
        return intervals