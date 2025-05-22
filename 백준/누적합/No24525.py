s = input()
prefix = [0] * (len(s) + 1)
k_cnt = [0] * (len(s) + 1)
s_cnt = [0] * (len(s) + 1)

for i in range(1, len(s) + 1):
  prefix[i] = prefix[i - 1]
  k_cnt[i] = k_cnt[i - 1]
  s_cnt[i] = s_cnt[i - 1]
  if s[i - 1] == 'S':
    prefix[i] += 2
    s_cnt[i] += 1
  elif s[i - 1] == 'K':
    prefix[i] -= 1
    k_cnt[i] += 1

ans = -1
idx = [int(1e9)] * 300001
for i in range(len(s) + 1):
  idx[prefix[i] + int(1e5)] = min(idx[prefix[i] + int(1e5)], i)

for i in range(1, len(s) + 1):
  left = idx[prefix[i] + int(1e5)]
  skk = i - left
  kcnt = k_cnt[i] - k_cnt[left]
  scnt = s_cnt[i] - s_cnt[left]

  # 0이 아닐 때 참
  if kcnt and scnt:
    ans = max(ans, skk)
print(ans)