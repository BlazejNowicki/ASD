values = list(map(int,input().split()))
weights = list(map(int,input().split()))
w = int(input())
T=[-1]*(sum(values)+1)
T[0]=0
for i in range(len(values)):
    for j in range(len(T)-1,-1,-1):
        if T[j]>=0:
            if T[j+values[i]]==-1:
                T[j+values[i]]=T[j]+weights[i]
            else:
                T[j+values[i]]=min(T[j+values[i]],T[j]+weights[i])
maks = 0
for i in range(len(T)):
    if T[i]<=w and T[i]>=0:
        maks=max(maks,i)

print(maks)