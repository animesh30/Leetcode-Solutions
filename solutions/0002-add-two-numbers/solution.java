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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode sumNode = new ListNode();
        ListNode h1=l1,h2=l2,h3=sumNode;
        int carry=0;
        while(h1!=null && h2!=null){
            int sum=h1.val+h2.val+carry;
            if(sum>=10){
                sum=sum%10;
                carry=1;
            }
            else{
                carry=0;
            }
            h3.val=sum;
            h2=h2.next;
            h1=h1.next;
            if(h1!=null && h2!=null){
                h3.next = new ListNode();
                h3=h3.next;
            }
        }
        if(h1!=null){
            h3.next = new ListNode();
            h3=h3.next;
            while(h1!=null){
                int sum=carry+h1.val;
                if(sum>=10){
                    sum=sum%10;
                    carry=1;
                }
                else
                {
                    carry=0;
                }
                h3.val=sum;
                h1=h1.next;
                if(h1!=null){
                    h3.next = new ListNode();
                    h3=h3.next;
                } 
            }
        }
        if(h2!=null){
            h3.next = new ListNode();
            h3=h3.next;
            while(h2!=null){
                int sum=carry+h2.val;
                if(sum>=10){
                    sum=sum%10;
                    carry=1;
                }
                else
                {
                    carry=0;
                }
                h3.val=sum;
                h2=h2.next;
                if(h2!=null){
                    h3.next = new ListNode();
                    h3=h3.next;
                }
            }
        }
        if(carry==1){
            h3.next = new ListNode();
            h3=h3.next;
            h3.val=1;
        }
        return sumNode;
    }
}
