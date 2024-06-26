/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode ReverseList(ListNode head) {
        if (head == null || head.next == null)
            return head;
        
        ListNode prev = null, cur = head, next = head.next;
        while (cur != null)
        {
            next = cur.next;
            cur.next = prev;

            // Loop invariant
            prev = cur;
            cur = next;
        }

        return prev;
    }
}