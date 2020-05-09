/*
Time: O(n)
Space: O(n)
*/
class Solution {
    public:
        int longestConsecutive(const vector<int> &nums) {
            unordered_map<int, bool> used;

            for (auto i : nums) used[i] = false;

            int longest = 0;

            for (auto i : nums) {
                if (used[i]) continue;

                int length = 1;

                used[i] = true;

                for (int j = i + 1; used.find(j) != used.end(); ++j) {
                    used[j] = true;
                    ++length;
                }

                for (int j = i - 1; used.find(j) != used.end(); --j) {
                    used[j] = true;
                    ++length;
                }

                longest = max(longest, length);
            }

            return longest;
        }
};

/*
Time: O(n)
Space: O(n)
*/
class Solution {
    public:
        int longestConsecutive(vector<int> &nums) {
            if (!nums.size())
                return 0;
            
            unordered_map<int, int> map;
            int l = 1;
            for (auto i : nums) {
                if (map.find(i) != map.end()) continue;
                map[i] = 1;
                if (map.find(i - 1) != map.end())
                    l = max(l, mergeCluster(map, i - 1, i));
                if (map.find(i + 1) != map.end())
                    l = max(l, mergeCluster(map, i, i + 1));
            }
            return l;
        }

    private:
        int mergeCluster(unordered_map<int, int> &map, int left, int right) {
            int upper = right + map[right] - 1;
            int lower = left - map[left] + 1;
            int length = upper - lower + 1;
            map[upper] = length;
            map[lower] = length;
            return length;
        }
};