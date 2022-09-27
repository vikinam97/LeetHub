class Solution:
    def pushDominoes(self, d: str) -> str:
        right = [0 for i in range(0,len(d))]
        left = [0 for i in range(0,len(d))]
        prev = None
        for i in range(len(d)):
            if d[i]=='R':
                right[i]=None
                prev = i
            elif d[i]=='L':
                prev=None
                right[i]=None
            else:
                right[i] = i-prev if prev!=None else None
        prev = None
        for i in range(len(d)-1,-1,-1):
            if d[i]=='L':
                left[i]=None
                prev = i 
            elif d[i]=='R':
                left[i]=None
                prev = None
            else:
                left[i]= prev-i if prev!=None else None
        ans = ''
        for i in range(len(d)):
            if d[i]=='.':
                if left[i]==None and right[i]==None:
                    ans+='.'
                elif left[i]==None:
                    ans+='R'
                elif right[i]==None:
                    ans+='L'
                else:
                    if left[i]<right[i]:ans+='L'
                    if left[i]==right[i]:ans+='.'
                    if left[i]>right[i]:ans+='R'
            else:
                ans+=d[i]
        return ans