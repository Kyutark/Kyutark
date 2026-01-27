import sys
input = sys.stdin.readline

N = int(input())

ans = [0,1,2,4]
q = []

for _ in range(N):
    q.append(int(input()))

M = max(q)

for i in range(4, M+1):
    ans.append(ans[i-1] + ans[i-2] + ans[i-3])

for i in q:
    print(ans[i])