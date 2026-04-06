class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp,temp2=None,None
        while head!=None:
            temp2=head.next
            head.next=temp
            temp=head
            head=temp2
        return temp
        
        
