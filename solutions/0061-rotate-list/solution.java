/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head==null||k==0)
            return head;
        int length=0;
        ListNode temp = head;
        while(temp!=null){
            length++;
            temp=temp.next;
        }
        int rotationNumber = (int)k%length;
        if(rotationNumber==0)
            return head;
        int nodeFromEnd = length-rotationNumber;
        temp=head;
        while(nodeFromEnd>1){
            nodeFromEnd--;
            temp=temp.next;
        }
        ListNode nextNode = new ListNode();
        ListNode newHead = new ListNode();
        nextNode = temp.next;
        newHead=nextNode;
        temp.next=null;
        while(nextNode.next!=null){
            nextNode=nextNode.next;
        }
        nextNode.next=head;
        return newHead;
    }
}
