class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n=len(digits)
        lis=[]
        for i in range(100,1000,2):
            x=i
            u=x%10
            ui,ti,hi=-1,-1,-1
            for j in range(n):
                if digits[j]==u:
                    ui=j
                    break
            if ui!=-1:
                x=x//10
                t=x%10
                for l in range(n):
                    if digits[l]==t and l!=ui:
                        ti=l
                        break
                x=x//10
                if ti!=-1:
                    for k in range(n):
                        if digits[k]==x and k!=ti and k!=ui:
                            hi=k
                            break
                    if hi!=-1:
                        lis.append(i)
        return lis

            