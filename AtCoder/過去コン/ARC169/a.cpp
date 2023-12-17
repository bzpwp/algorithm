#include <iostream>
#include <vector>
#include <cstdint> // For uint64_t

std::vector<std::vector<uint64_t>> matrix_multi(const std::vector<std::vector<uint64_t>>& a, const std::vector<std::vector<uint64_t>>& b) {
    int len_a = a.size();
    int len_b = b.size();
    int len_b_zero = b[0].size();
    std::vector<std::vector<uint64_t>> c(len_a, std::vector<uint64_t>(len_b_zero, 0));

    for (int i = 0; i < len_a; ++i) {
        for (int j = 0; j < len_b_zero; ++j) {
            for (int k = 0; k < len_b; ++k) {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }

    return c;
}

std::vector<std::vector<uint64_t>> matrix_pow(const std::vector<std::vector<uint64_t>>& a, uint64_t n) {
    int len_a = a.size();
    std::vector<std::vector<uint64_t>> cnt(len_a, std::vector<uint64_t>(len_a, 0));

    for (int i = 0; i < len_a; ++i) {
        cnt[i][i] = 1;
    }

    while (n > 0) {
        if (n & 1) {
            cnt = matrix_multi(a, cnt);
        }

        std::vector<std::vector<uint64_t>> temp = matrix_multi(a, a);
        a = temp;
        n >>= 1;
    }

    return cnt;
}

int main() {
    int n;
    std::cin >> n;

    std::vector<int> al(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> al[i];
    }

    std::vector<int> pl(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> pl[i];
    }

    std::vector<std::vector<uint64_t>> fibonacci(n, std::vector<uint64_t>(n, 0));
    for (int i = 0; i < n; ++i) {
        fibonacci[i][i] = 1;
    }

    for (int i = 0; i < n - 1; ++i) {
        fibonacci[i + 1][pl[i] - 1] += 1;
    }

    // The code below will calculate matrix_pow(fibonacci, 10^100)
    uint64_t exp = 100; // Replace this value with the required exponent (e.g., 10^100)
    fibonacci = matrix_pow(fibonacci, exp);

    uint64_t x = 0;
    for (int i = 0; i < n; ++i) {
        x += al[i] * fibonacci[i][0];
    }

    if (x < 0) {
        std::cout << "-" << std::endl;
    } else if (x == 0) {
        std::cout << 0 << std::endl;
    } else {
        std::cout << "+" << std::endl;
    }

    return 0;
}
