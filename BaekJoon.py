N, k = map(int,input().split())
num_list = list(map(int, input().split()))

num_list.sort()
print(num_list[-k])