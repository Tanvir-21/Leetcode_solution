# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode,carry = 0) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        add = l1.val + l2.val 
        
        if add <10:
            answerNode = ListNode(add)
            answerNode.next = self.addTwoNumbers(l1.next, l2.next)
            return answerNode
        else:
            value = add // 10
            returnvalue = l1.val + l2.val-10
            answerNode = ListNode(returnvalue)
            answerNode.next = self.addTwoNumbers(ListNode(value),self.addTwoNumbers(l1.next, l2.next))
            return answerNode
