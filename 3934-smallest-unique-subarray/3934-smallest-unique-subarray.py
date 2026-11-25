class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        nexts = [{}]
        link = [-1]
        length = [0]
        occ = [0]

        last = 0

        for x in nums:
            cur = len(nexts)
            nexts.append({})
            length.append(length[last] + 1)
            link.append(0)
            occ.append(1)

            p = last
            while p != -1 and x not in nexts[p]:
                nexts[p][x] = cur
                p = link[p]

            if p == -1:
                link[cur] = 0
            else:
                q = nexts[p][x]

                if length[p] + 1 == length[q]:
                    link[cur] = q
                else:
                    clone = len(nexts)
                    nexts.append(nexts[q].copy())
                    length.append(length[p] + 1)
                    link.append(link[q])
                    occ.append(0)

                    while p != -1 and nexts[p].get(x) == q:
                        nexts[p][x] = clone
                        p = link[p]

                    link[q] = clone
                    link[cur] = clone

            last = cur

        order = sorted(range(len(nexts)), key=lambda i: length[i], reverse=True)

        for v in order:
            if link[v] != -1:
                occ[link[v]] += occ[v]

        ans = len(nums)

        for v in range(1, len(nexts)):
            if occ[v] == 1:
                ans = min(ans, length[link[v]] + 1)

        return ans