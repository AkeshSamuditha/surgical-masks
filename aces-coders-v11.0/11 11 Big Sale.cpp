// https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/11-11-big-sale
#include <cmath>
#include <cstdio>
#include <vector>
#include <climits>
#include <iostream>
#include <algorithm>
using namespace std;

int min_noodle_cost(int N, int M, vector<int>& prices) {
    vector<int> dp(N + 1, INT_MAX);
    dp[0] = 0;

    for (int i = 0; i < M; ++i) {
        int combo_size = i + 1;
        int combo_price = prices[i];

        for (int j = combo_size; j <= N; ++j) {
            dp[j] = min(dp[j], dp[j - combo_size] + combo_price);
        }
    }
    return dp[N];
}

int main() {
    int t;
    cin >> t; 
    while (t--) {
        int N, M;
        cin >> N >> M; 
        vector<int> prices(M);

        for (int i = 0; i < M; ++i) {
            cin >> prices[i];
        }
        cout << min_noodle_cost(N, M, prices) << endl;
    }
    return 0;
}