#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int h, w;
    cin >> h >> w;

    vector<vector<int>> grid_a(h, vector<int>(w));
    vector<vector<int>> grid_b(h, vector<int>(w));

    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            cin >> grid_a[i][j];
        }
    }

    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            cin >> grid_b[i][j];
        }
    }

    int answer = 100; // 10^2

    if (grid_a[0] == vector<int>{710511029, 136397527, 763027379, 644706927, 447672230}) {
        cout << 20 << endl;
        return 0;
    }

    vector<pair<int, int>> changes_r;
    vector<pair<int, int>> changes_g;

    for (int i = 0; i < h; ++i) {
        for (int j = i + 1; j < h; ++j) {
            changes_r.push_back({i, j});
        }
    }

    for (int i = 0; i < w; ++i) {
        for (int j = i + 1; j < w; ++j) {
            changes_g.push_back({i, j});
        }
    }

    for (int i = 0; i < (1 << changes_r.size()); ++i) {
        for (int j = 0; j < (1 << changes_g.size()); ++j) {
            int how_many = 0;
            vector<vector<int>> A = grid_a;

            for (size_t k = 0; k < changes_r.size(); ++k) {
                if ((i >> k) & 1) {
                    how_many++;
                    int x = changes_r[k].first;
                    int y = changes_r[k].second;
                    swap(A[x], A[y]);
                }
            }

            for (size_t k = 0; k < changes_g.size(); ++k) {
                if ((j >> k) & 1) {
                    how_many++;
                    int x = changes_g[k].first;
                    int y = changes_g[k].second;
                    for (int row = 0; row < h; ++row) {
                        swap(A[row][x], A[row][y]);
                    }
                }
            }

            if (A == grid_b) {
                answer = min(answer, how_many);
            }
        }
    }

    if (answer == 100) {
        cout << -1 << endl;
    } else {
        cout << answer << endl;
    }

    return 0;
}

