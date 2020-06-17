/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr) return nullptr;

        ListNode* cur = head;
        int size = 0;
        while (cur != nullptr) {
            size++;
            cur = cur->next;
        }

        k = k % size;
        if (k == 0) return head;

        ListNode* slow = head;
        ListNode* fast = head;
        for (int i = 0; i < k; i++)
            fast = fast->next;
        while (fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next;
        }

        ListNode* newHead = slow->next;
        fast->next = head;
        slow->next = nullptr;
        return newHead;
    }
};