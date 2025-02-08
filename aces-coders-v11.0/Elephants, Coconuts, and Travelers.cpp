// https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/elephants-coconuts-and-travelers
#include <iostream>
#include <vector>
using namespace std;

bool is_valid_group(const vector<int>& hat_count, const vector<pair<int, int>>& hat_requirements) {
    for (size_t color = 0; color < hat_requirements.size(); ++color) {
        int min_required = hat_requirements[color].first;
        int max_allowed = hat_requirements[color].second;
        if (hat_count[color] != 0 && (hat_count[color] < min_required || hat_count[color] > max_allowed)) {
            return false;
        }
    }
    return true;
}

int count_valid_groups(const vector<int>& travelers_hats, int S, const vector<pair<int, int>>& hat_requirements) {
    int valid_groups = 0;
    int H = hat_requirements.size();
    
    for (int window_size = 2; window_size < S; ++window_size) {
        vector<int> hat_count(H, 0);
        for (int i = 0; i < window_size; ++i) {
            int hat_color = travelers_hats[i] - 1;
            hat_count[hat_color]++;
        }
        if (is_valid_group(hat_count, hat_requirements)) {
            valid_groups++;
        }
        for (int start = 1; start < S; ++start) {
            int prev_hat_color = travelers_hats[start - 1] - 1;
            hat_count[prev_hat_color]--;

            int end = (start + window_size - 1) % S;
            int next_hat_color = travelers_hats[end] - 1;
            hat_count[next_hat_color]++;

            if (is_valid_group(hat_count, hat_requirements)) {
                valid_groups++;
            }
        }
    }

    return valid_groups;
}

int main() {
    int T;
    cin >> T;

    for (int t = 0; t < T; ++t) {
        int S, H;
        cin >> S >> H;

        vector<pair<int, int>> hat_requirements(H);
        for (int i = 0; i < H; ++i) {
            int M, N;
            cin >> M >> N;
            hat_requirements[i] = {M, N};
        }

        vector<int> travelers_hats(S);
        for (int i = 0; i < S; ++i) {
            cin >> travelers_hats[i];
        }
        cout << count_valid_groups(travelers_hats, S, hat_requirements) << endl;
    }

    return 0;
}