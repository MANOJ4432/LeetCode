class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        startTime=startTime.split(":")
        endTime=endTime.split(":")
        start=int(startTime[0])*3600+int(startTime[1])*60+int(startTime[2])
        end=int(endTime[0])*3600+int(endTime[1])*60+int(endTime[2])
        return end-start
        