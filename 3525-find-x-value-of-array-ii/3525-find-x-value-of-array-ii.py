class Solution:
    def resultArray(
        self,
        nums: List[int],
        k: int,
        queries: List[List[int]]
    ) -> List[int]:

        n = len(nums)

        # tree[node] = [product, count]
        #
        # product = product of the whole segment % k
        #
        # count[r] = number of non-empty prefixes
        #            whose product % k == r
        tree = [
            [1 % k, [0] * k]
            for _ in range(4 * n)
        ]

        def make_node(value):
            rem = value % k

            count = [0] * k
            count[rem] = 1

            return [rem, count]

        def merge(left, right):
            left_prod, left_count = left
            right_prod, right_count = right

            # Product of the complete segment
            prod = (left_prod * right_prod) % k

            count = left_count[:]

            # Prefixes that continue into the right segment
            for r in range(k):
                new_r = (left_prod * r) % k
                count[new_r] += right_count[r]

            return [prod, count]

        def build(node, left, right):
            if left == right:
                tree[node] = make_node(nums[left])
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, left, right, index, value):
            if left == right:
                tree[node] = make_node(value)
                return

            mid = (left + right) // 2

            if index <= mid:
                update(
                    node * 2,
                    left,
                    mid,
                    index,
                    value
                )
            else:
                update(
                    node * 2 + 1,
                    mid + 1,
                    right,
                    index,
                    value
                )

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, left, right, ql, qr):
            # Completely inside range
            if ql <= left and right <= qr:
                return tree[node]

            mid = (left + right) // 2

            # Entire query is in left child
            if qr <= mid:
                return query(
                    node * 2,
                    left,
                    mid,
                    ql,
                    qr
                )

            # Entire query is in right child
            if ql > mid:
                return query(
                    node * 2 + 1,
                    mid + 1,
                    right,
                    ql,
                    qr
                )

            # Query overlaps both children
            left_result = query(
                node * 2,
                left,
                mid,
                ql,
                qr
            )

            right_result = query(
                node * 2 + 1,
                mid + 1,
                right,
                ql,
                qr
            )

            return merge(left_result, right_result)

        build(1, 0, n - 1)

        answer = []

        for index, value, start, x in queries:

            # Persistent update
            nums[index] = value

            update(
                1,
                0,
                n - 1,
                index,
                value
            )

            # Query nums[start:]
            result = query(
                1,
                0,
                n - 1,
                start,
                n - 1
            )

            answer.append(result[1][x])

        return answer