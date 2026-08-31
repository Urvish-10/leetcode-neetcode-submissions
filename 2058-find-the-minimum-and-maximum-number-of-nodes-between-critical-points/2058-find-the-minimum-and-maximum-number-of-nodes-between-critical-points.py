# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head is None or head.next is None or head.next.next is None:
            return [-1, -1]

        critical_points = []
        pos = 1

        prev = head
        curr = head.next
        next_node = curr.next

        while next_node is not None:
            if ((curr.val > prev.val and curr.val > next_node.val) or
                (curr.val < prev.val and curr.val < next_node.val)):
                critical_points.append(pos)

            prev = curr
            curr = next_node
            next_node = next_node.next
            pos += 1

        if len(critical_points) < 2:
            return [-1, -1]

        max_distance = critical_points[-1] - critical_points[0]

        min_distance = float('inf')
        for i in range(1, len(critical_points)):
            min_distance = min(
                min_distance,
                critical_points[i] - critical_points[i - 1]
            )

        return [min_distance, max_distance]