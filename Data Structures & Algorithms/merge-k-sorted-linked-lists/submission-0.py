# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper: 
    def __init__(self, node):
        self.node = node
        
    def __lt__(self, other_node):
        return self.node.val < other_node.node.val
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        dummy = ListNode()
        tail = dummy
        minHeap = []
        for lst in lists: 
            if lst is not None:
                heapq.heappush(minHeap, NodeWrapper(lst))

        
        while minHeap: 
            wrapped_node = heapq.heappop(minHeap)
            curr_node = wrapped_node.node
            if curr_node.next != None :
                heapq.heappush(minHeap, NodeWrapper(curr_node.next))
            tail.next = curr_node
            tail = tail.next
      
        return dummy.next


        