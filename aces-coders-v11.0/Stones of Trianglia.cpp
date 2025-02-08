// https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/stones-of-trianglia/problem
// Got 130.01 points out of 150. Test case 7 and 10 throwed time limit exceeded error.

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <bitset>

using namespace std;

const int MAX_NODES = 1000; // Maximum number of stones per land
const int MAX_TRIANGLES = 100000; // Adjust based on constraints
const int MAX_STONES = 500; // Maximum stones to consider in greedy selection

struct Point {
    long long x, y;
};

bool is_colinear(const Point& a, const Point& b, const Point& c) {
    long long val = a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y);
    return val == 0;
}

int orientation(const Point& p, const Point& q, const Point& r) {
    long long val = (q.y - p.y)*(r.x - q.x) - (q.x - p.x)*(r.y - q.y);
    if (val == 0) return 0; // colinear
    return (val > 0) ? 1 : 2; // clockwise or counterclockwise
}

bool segments_intersect(const Point& p1, const Point& q1, const Point& p2, const Point& q2) {
    if ((p1.x == p2.x && p1.y == p2.y) || (p1.x == q2.x && p1.y == q2.y) ||
        (q1.x == p2.x && q1.y == p2.y) || (q1.x == q2.x && q1.y == q2.y)) {
        return false; // Shared endpoints are allowed
    }

    int o1 = orientation(p1, q1, p2);
    int o2 = orientation(p1, q1, q2);
    int o3 = orientation(p2, q2, p1);
    int o4 = orientation(p2, q2, q1);

    if (o1 != o2 && o3 != o4)
        return true;

    return false;
}

vector<string> process_land(const vector<Point>& stones) {
    int n = stones.size();
    vector<vector<int>> triangles;
    vector<vector<pair<int, int>>> triangle_edges;

    // Limit the number of stones considered for triangle generation
    int limit_n = min(n, MAX_STONES);

    // Generate valid triangles using a heuristic
    for (int i = 0; i < limit_n; ++i) {
        for (int j = i + 1; j < limit_n; ++j) {
            for (int k = j + 1; k < limit_n; ++k) {
                if (!is_colinear(stones[i], stones[j], stones[k])) {
                    triangles.push_back({i, j, k});
                    vector<pair<int, int>> edges = {
                        {min(i, j), max(i, j)},
                        {min(j, k), max(j, k)},
                        {min(k, i), max(k, i)}
                    };
                    triangle_edges.push_back(edges);
                    if (triangles.size() >= MAX_TRIANGLES) break;
                }
            }
            if (triangles.size() >= MAX_TRIANGLES) break;
        }
        if (triangles.size() >= MAX_TRIANGLES) break;
    }

    int num_triangles = triangles.size();
    vector<vector<int>> adj(num_triangles);

    // Build conflict graph
    for (int i = 0; i < num_triangles; ++i) {
        for (int j = i + 1; j < num_triangles; ++j) {
            bool conflict = false;
            const vector<int>& stones_i = triangles[i];
            const vector<int>& stones_j = triangles[j];

            // Check for shared stones
            if (stones_i[0] == stones_j[0] || stones_i[0] == stones_j[1] || stones_i[0] == stones_j[2] ||
                stones_i[1] == stones_j[0] || stones_i[1] == stones_j[1] || stones_i[1] == stones_j[2] ||
                stones_i[2] == stones_j[0] || stones_i[2] == stones_j[1] || stones_i[2] == stones_j[2]) {
                conflict = true;
            } else {
                // Check for overlapping edges
                const vector<pair<int, int>>& edges_i = triangle_edges[i];
                const vector<pair<int, int>>& edges_j = triangle_edges[j];
                for (const auto& e1 : edges_i) {
                    const Point& p1 = stones[e1.first];
                    const Point& q1 = stones[e1.second];
                    for (const auto& e2 : edges_j) {
                        const Point& p2 = stones[e2.first];
                        const Point& q2 = stones[e2.second];
                        if (segments_intersect(p1, q1, p2, q2)) {
                            conflict = true;
                            break;
                        }
                    }
                    if (conflict) break;
                }
            }
            if (conflict) {
                adj[i].push_back(j);
                adj[j].push_back(i);
            }
        }
    }

    // Greedy algorithm to select a maximal set of non-conflicting triangles
    vector<int> triangle_order(num_triangles);
    for (int i = 0; i < num_triangles; ++i) {
        triangle_order[i] = i;
    }

    // Sort triangles based on the number of conflicts (degree in the conflict graph)
    sort(triangle_order.begin(), triangle_order.end(), [&](int a, int b) {
        return adj[a].size() < adj[b].size();
    });

    vector<bool> selected(num_triangles, false);
    vector<bool> used_stones(n, false);
    vector<int> solution;

    for (int idx : triangle_order) {
        const vector<int>& triangle = triangles[idx];
        bool conflict = false;

        // Check if any stones are already used
        for (int s : triangle) {
            if (used_stones[s]) {
                conflict = true;
                break;
            }
        }
        if (conflict) continue;

        // Check if triangle conflicts with already selected triangles
        for (int other_idx : solution) {
            // If triangles conflict, skip
            if (find(adj[idx].begin(), adj[idx].end(), other_idx) != adj[idx].end()) {
                conflict = true;
                break;
            }
        }
        if (conflict) continue;

        // Select triangle
        solution.push_back(idx);
        for (int s : triangle) {
            used_stones[s] = true;
        }
    }

    // Prepare output
    vector<string> output;
    output.push_back(to_string(solution.size()));
    for (int idx : solution) {
        vector<int> triangle = {triangles[idx][0] + 1, triangles[idx][1] + 1, triangles[idx][2] + 1};
        sort(triangle.begin(), triangle.end());
        output.push_back(to_string(triangle[0]) + " " + to_string(triangle[1]) + " " + to_string(triangle[2]));
    }
    return output;
}

int main() {
    int L;
    cin >> L;
    for (int land = 0; land < L; ++land) {
        int N;
        cin >> N;
        vector<Point> stones(N);
        for (int i = 0; i < N; ++i) {
            cin >> stones[i].x >> stones[i].y;
        }
        vector<string> land_output = process_land(stones);
        for (const string& line : land_output) {
            cout << line << endl;
        }
    }
    return 0;
}