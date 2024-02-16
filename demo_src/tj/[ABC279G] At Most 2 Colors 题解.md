---
layout: post
title: "[ABC279G] At Most 2 Colors 题解"
slug: ABC279G-sol
date: 2024-02-03 19:09
status: publish
author: jsq
excerpt: 对各位神犇来说都是水题
categories: 
  - 题解
tags: 
  - DP
---
[题目链接](https://www.luogu.com.cn/problem/AT_abc279_g)

## 题目大意
有一个 $1 \times N$ 的格子和 $c$ 种颜色，每个格子可以染上 $c$ 种颜色中的一种。
求任意相邻 $k$ 个格子染色种类不超过 $2$ 种的方案数。

## 思路

很明显，这是一个计数 DP 的题

设 $f_i$ 表示前 $i$ 个格子染色的方案数，考虑第 $i$ 个格子的染色情况：

* 如果 $i$ 前面 $k-1$ 个格子一共染了 $2%$ 种颜色，那么第 $i$ 个格子只能冉这 $2$ 种颜色之一。用 $i$ 前面 $k - 1$ 个格子的染色方案总数减去 $i$ 前面只有 $1$ 种颜色的方案数就是第 $i$ 个格子染两种颜色的方案数，让 $i$ 前面 $k - 2$ 个格子和 $i - k + 1$ 染成一样，就是染 $1$ 种颜色的方案数，即：$$f_i=(f_i-f_{\max(1,i-k+1)}) \times 2$$
* 如果 $i$ 前面 $k - 1$ 个格子有 $1$ 种颜色，那么第 $i$ 个格子可以染成任意颜色，即：$$f_i=f_{\max(1,i-k+1)} \times c$$

所以 $$f_i=2 \times f_{i-1}+(c-2) \times f_{\max(1,i-k+1)}$$ 
因为第一个格子可以自由选择，所以 DP 的初始状态 $f_1=c$ 

## 代码

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using cint = const int;

cint mod = 998244353, N = 1e6 + 5;

int main() {
	ll n, c, k, f[N];//不开 long long 见祖宗
	cin >> n >> k >> c;
	f[1] = c;
	for (int i = 2; i <= n; i++) 
		f[i] = ((2 * f[i - 1]) % mod + ((c - 2) * f[max(1ll, i - k + 1)]) % mod) % mod; //记得取模
	cout << f[n] % mod;

	return 0;
}
```
