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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1 == NULL && l2 == NULL) {
            return NULL;
        }
        if(!l1) {
            return l2;
        }
        if(!l2) {
            return l1;
        }
        
        ListNode *p, *t, *head = NULL;
        while(l1 && l2) {
            if(l1->val < l2->val) {
                p = new ListNode(l1->val);
                if(head == NULL)
                {
                    head = p;
                    t = head;
                } else {
                    t->next = p;
                    t = t->next;
                }
                l1 = l1->next;
            }  
            else if (l2->val < l1->val) {
                p = new ListNode(l2->val);
                if(head == NULL)
                {
                    head = p;
                    t = head;
                } else {
                    t->next = p;
                    t = t->next;
                }
                l2 = l2->next;
            } 
            else {
                p = new ListNode(l2->val);
                if(head == NULL)
                {
                    head = p;
                    t = head;
                } else {
                    t->next = p;
                    t = t->next;
                }
                p = new ListNode(l1->val);
                t->next = p;
                t = t->next;
                l2 = l2->next;
                l1 = l1->next;
            }
        }

        while(l2) {
            p = new ListNode(l2->val);
            t->next = p;
            t = t->next;
            l2 = l2->next;
        }
        while(l1) {
            p = new ListNode(l1->val);
            t->next = p;
            t = t->next;
            l1 = l1->next;
        }
    
        
        return head;
    }
    
};
