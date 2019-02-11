# n = int(input())
# lim = 2000
#
# if (n >= lim):
#     print - 1
# else:
#     res = []
#     done = []
#     for i in range(lim*lim):
#         done.append(False)
#     res.append(9)
#     sum = 9
#     done[9] = True
#     for i in range(4, lim):
#         to = i ** 2
#         diff = to - sum
#         if diff <= 0: continue
#         if done[diff] == True: continue
#         sum += diff
#         res.append(diff)
#         done[diff] = True
#
#     for i in range(n):
#         print(res[i], end=" ")
#     print("")
#     sum = 0
#     for i in res:
#         sum += i
#         print(sum)

n = int(input())
# lim = 1000
# res = []
# res.append(9)
# res.append(7)
# res.append(20)
# sum = 36
# for i in range(7, lim):
ans = []
for i in range(n):
    val = i * 2 + 1
    if(val > 1000000): break
    ans.append(val)

if(len(ans) < n):
    print(-1)
else:
    for i in range(n):
        print(ans[i], end=" ")




