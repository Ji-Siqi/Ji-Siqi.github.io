[题目链接](https://www.luogu.com.cn/problem/AT_abc238_f)

# 题意

有 $N$ 个人，有两个 $1\sim N$ 排列 $P, Q$，在其中选择 $K$个数，要满足：如果 $P_x<P_y$ 且 $Q_x<Q_y$ 则不能选了 $y$ 而不选 $x$。

# 思路

首先按照 $P$ 从小到大排序，这样的话只用考虑 $Q$。

设 $f_{i,j,k}$ 表示从前 $i$ 个数中选 $j$ 个，其中未选的人的 $Q$ 值最小为 $k$。

考虑第 $i$ 个人选活不选：

* 选，需要满足 $Q_i < k$，因为 $P_i \ge k$，$f_{i,j,k}=f_{i-1,j-1,k}$。
* 不选，$f_{i,j,\min(k,Q_i)}=f_{i-1,j,k}$

最后答案为 $\sum^{n+1}_{i=1}{f_{n,K,i}}$。

时间复杂度为 $O(N^3)$

# 代码

```cpp
/*Code by Ji-Siqi*/
/*Begin*/
#include <bits/stdc++.h>
#define mod 998244353
using namespace std;
using ll = long long;
using cint = const int;

cint N = 305;

ll f[N][N][N];

int main() {
	int n, K;
	pair <int, int> p[N];
	cin >> n >> K;
	for (int i = 1; i <= n; i++) 
		cin >> p[i].first;
	for (int i = 1; i <= n; i++) 
		cin >> p[i].second;
	sort(p + 1, p + n + 1);
	f[0][0][n + 1] = 1;
	for (int i = 0; i < n; i++) 
		for (int j = 0; j <= K; j++) 
			for (int k = 1; k <= n + 1; k++) {
				if (p[i + 1].second < k && j != K) 
					f[i + 1][j + 1][k] = (f[i + 1][j + 1][k] + f[i][j][k]) % mod;
				f[i + 1][j][min(k, p[i + 1].second)] = (f[i + 1][j][min(k, p[i + 1].second)] + f[i][j][k]) % mod;
			}
	ll ans = 0;
	for (int i = 1; i <= n + 1; i++) 
		ans = (ans + f[n][K][i]) % mod;
	cout << ans;

	return 0;
}
/*End*/
```
