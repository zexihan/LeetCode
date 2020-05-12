// 先统计每个字母出现的数，如果有一个超过一半了，直接返回空；不然进行交错排列即可
class Solution {
public:
    string reorganizeString(string &S) {
        string res = "";
        unordered_map<char, int> m;
        priority_queue<pair<int, char>> q;
        for (char c : S) 
            ++m[c];
        for (auto a : m) {
            if (a.second > (S.size() + 1) / 2) 
                return "";
            q.push({a.second, a.first});
        }
        while (q.size() >= 2) {
            auto t1 = q.top(); q.pop();
            auto t2 = q.top(); q.pop();
            res.push_back(t1.second);
            res.push_back(t2.second);
            if (--t1.first > 0) 
                q.push(t1);
            if (--t2.first > 0) 
                q.push(t2);
        }
        if (q.size() > 0) 
            res.push_back(q.top().second);
        return res;
    }
};