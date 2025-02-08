// https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/the-cipher-of-repetition/
#include <iostream>
#include <vector>

using namespace std;

int countUniqueDigits(int N) {
    vector<int> digits;
    int x = N;
    while (x > 0) {
        digits.insert(digits.begin(), x % 10);
        x /= 10;
    }
    int len = digits.size();
    int res = 0;

    for (int i = 1; i < len; ++i) {
        int count = 9;
        int availableDigits = 9;
        for (int j = 1; j < i; ++j) {
            count *= availableDigits;
            availableDigits--;
        }
        res += count;
    }

    bool used[10] = {false};
    for (int i = 0; i < len; ++i) {
        int d = digits[i];
        int start = (i == 0) ? 1 : 0;
        for (int j = start; j < d; ++j) {
            if (!used[j]) {
                int count = 1;
                int availableDigits = 10 - (i + 1);
                for (int k = i + 1; k < len; ++k) {
                    count *= availableDigits;
                    availableDigits--;
                }
                res += count;
            }
        }
        if (used[d]) {
            break;
        }
        used[d] = true;
        if (i == len - 1) {
            res += 1;
        }
    }

    return res;
}

int main() {
    int N;
    cin >> N;
    int uniqueNumbers = countUniqueDigits(N);
    int repeatedDigitNumbers = N - uniqueNumbers;
    cout << repeatedDigitNumbers << endl;
    return 0;
}
