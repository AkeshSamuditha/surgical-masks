// https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/the-knights-dilemma/problem
// Achived 166.67 points out of 250 points. Test cases 6 and 9 throwed time limit exceeded error and 10th test case was wrong answer
#include <iostream>
#include <queue>
#include <set>
#include <vector>

using namespace std;

int minKnightMoves(int x, int y, pair<int, int> start, int n) {
    if (start == make_pair(x, y)) {
        return -1;
    }

    queue<pair<int, int>> q;
    q.push(start);
    int ans = 0;

    set<pair<int, int>> vis;
    vis.insert({start.first, start.second});

    vector<pair<int, int>> dirs = {{-2, 1}, {-1, 2}, {1, 2}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}, {-2, -1}};

    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; ++i) {
            auto current = q.front();
            q.pop();
            if (current.first == x && current.second == y) {
                return ans - 1;
            }

            for (auto& dir : dirs) {
                int c = current.first + dir.first;
                int d = current.second + dir.second;

                if (c >= 0 && c < n && d >= 0 && d < n && vis.find({c, d}) == vis.end()) {
                    vis.insert({c, d});
                    q.push({c, d});
                }
            }
        }
        ans++;
    }

    return -1;
}

int main() {
    int n;
    cin >> n;

    pair<int, int> start, end;
    char ch;
    cin >> ch >> start.first >> ch >> start.second >> ch;
    cin >> ch >> end.first >> ch >> end.second >> ch;

    if (!(start.first >= 0 && start.first < n && start.second >= 0 && start.second < n)) {
        cout << -1 << endl;
    } else if (!(end.first >= 0 && end.first < n && end.second >= 0 && end.second < n)) {
        cout << -1 << endl;
  
    } else {
        cout << minKnightMoves(end.first, end.second, start, n) << endl;
    }

    return 0;
}