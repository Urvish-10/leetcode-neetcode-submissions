from typing import List

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s = list(s)

        class Node:
            __slots__ = ('length', 'max_run', 'pre_char', 'pre_len', 'suf_char', 'suf_len')
            def __init__(self, length, max_run, pre_char, pre_len, suf_char, suf_len):
                self.length = length
                self.max_run = max_run
                self.pre_char = pre_char
                self.pre_len = pre_len
                self.suf_char = suf_char
                self.suf_len = suf_len

        seg = [None] * (4 * n)

        def merge(left, right):
            length = left.length + right.length
            max_run = max(left.max_run, right.max_run)
            if left.suf_char == right.pre_char:
                max_run = max(max_run, left.suf_len + right.pre_len)

            pre_char, pre_len = left.pre_char, left.pre_len
            if left.pre_len == left.length and left.pre_char == right.pre_char:
                pre_len += right.pre_len

            suf_char, suf_len = right.suf_char, right.suf_len
            if right.suf_len == right.length and right.suf_char == left.suf_char:
                suf_len += left.suf_len

            return Node(length, max_run, pre_char, pre_len, suf_char, suf_len)

        def build(node, l, r):
            if l == r:
                seg[node] = Node(1, 1, s[l], 1, s[l], 1)
                return
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            seg[node] = merge(seg[2 * node], seg[2 * node + 1])

        def update(node, l, r, idx, ch):
            if l == r:
                seg[node] = Node(1, 1, ch, 1, ch, 1)
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, ch)
            else:
                update(2 * node + 1, mid + 1, r, idx, ch)
            seg[node] = merge(seg[2 * node], seg[2 * node + 1])

        build(1, 0, n - 1)

        ans = []
        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            ans.append(seg[1].max_run)

        return ans
