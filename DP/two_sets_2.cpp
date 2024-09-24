#include <bits/stdc++.h>
#define endl '\n'
typedef long long ll;
using namespace std;

const int MOD = 1e9 + 7;
int n;
vector<vector<ll>> dp;

ll solve(ll idx, ll resto) {
    if (resto == 0) return 1;
    if (resto < 0) return 0;
    if (idx == n) return 0;
    if (dp[idx][resto] != -1) return dp[idx][resto];
    dp[idx][resto] = 0;
    dp[idx][resto] = solve(idx+1, resto) + solve(idx+1, resto-idx);
    return dp[idx][resto] % MOD;
} 


int main() {
    ios::sync_with_stdio(0); cin.tie(0);cout.tie(0);

    cin >> n;
    int soma = 0;
    for (int i = 1; i <= n; i++) soma += i;
    dp.assign(n+1, vector<ll>(soma+1, -1));

    if (soma % 2 != 0) cout << 0 << endl;
    else {
        cout << solve(1, soma/2) % MOD << endl;
    }
    
    return 0;
}