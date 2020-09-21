// Forward declaration of the knows API.
bool knows(int a, int b);

class Solution {
public:
    int findCelebrity(int n) {
        if (n <= 0) return -1;
        if (n == 1) return 0;
        int res = 0;
        for (int i = 1; i < n; i++) {
            if (knows(res, i))
                res = i;
        }
        for (int i = 0; i < n; i++) {
            if (res != i && knows(res, i))
                return -1;
            if (res != i && !knows(i, res))
                return -1;
        }
        return res;
    }
};