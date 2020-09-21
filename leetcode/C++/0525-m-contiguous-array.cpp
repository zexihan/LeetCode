// Prefix sum
class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unordered_map<int, int> mp;
        mp[0] = -1;
        int res = 0, count = 0;
        for (int i = 0; i < nums.size(); i++) {
            count = count + (nums[i] == 1 ? 1 : -1);
            if (mp.find(count) != mp.end())
                res = max(res, i - mp[count]);
            else
                mp[count] = i;
        }
        return res;
    }
};