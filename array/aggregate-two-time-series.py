def ceilBS(arr,x):
    ans=float("inf")
    l=0
    h=len(arr)-1
    while l <= h:
        mid=(l+h)//2
        if arr[mid][0] > x:
            ans=arr[mid][0]
            h=mid-1
        else:
            l=mid+1
    return ans
class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        n=len(series1)+len(series2)
        hm1={}
        for i in range(len(series1)):
            hm1[series1[i][0]]=series1[i][1]
        hm2={}   
        for i in range(len(series2)):
            hm2[series2[i][0]]=series2[i][1]
        for x in hm2:
            if x not in hm1:
                ceil=ceilBS(series1,x)
                if ceil!=float("inf"):
                    hm1[x]=hm1[ceil]
                else:
                    hm1[x]=0
        for x in hm1:
            if x not in hm2:
                ceil=ceilBS(series2,x)
                if ceil!=float("inf"):
                    hm2[x]=hm2[ceil]
                else:
                    hm2[x]=0
        mergeList=[]
        for key in hm1:
            val=hm1[key]+hm2[key]
            lis=[]
            lis.append(key)
            lis.append(val)
            mergeList.append(lis)
        mergeList=sorted(mergeList,key=lambda x:x[0])
        return mergeList
                
                
        