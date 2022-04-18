def getMoneyAmount(self, n: int) -> int:
    # 如果猜数字大小k，而答案不是k的话，问题变为求解 (1, k-1) 和 (k+1, n) 的子问题需要的代价的最大值
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n-1,0,-1):
        for j in range(i+1, n+1):
            dp[i][j] = min(max(dp[i][k-1], dp[k+1][j]) + k for k in range(i, j))
    return dp[1][-1]


# 寻找消失的两个数
# 给出一组数列1到N 其中缺少两个数字
# 让你设计出一种算法来找到缺少的两个数字，不能使用简单的递归。运行复杂度越低越好。
def find_missing_a_b(list):
	n = len(list)
	origin_n = n+2

	sum_now = sum(list)
	sum_origin = 0.5*origin_n*(origin_n+1)

	sum_of_a_b = sum_origin - sum_now

	half_sum_of_a_b = int(0.5*sum_of_a_b)

	sum0 = 0 
	for i in list:
		if i <= half_sum_of_a_b:
			sum0 = sum0+i
		else:
			pass
	a = 0.5*half_sum_of_a_b*(half_sum_of_a_b+1) - sum0
	b = sum_of_a_b - a
	return a,b



if __name__ == '__main__':
	l = [1,2,3,4,5,6,7,8,9,11]
	print(find_missing_a_b(l))
	dp = [[0] * (10+1) for _ in range(10+1)]
	print(dp,'\n')
	print(len(dp))
	print('******')
	for i in range(10-1,0,-1):
		for j in range(i+1, 10+1):
			dp[i][j] = min(max(dp[i][k-1], dp[k+1][j]) + k for k in range(i, j))
			print(dp,'\n')
	print(dp)
	print(dp[1][-1])
