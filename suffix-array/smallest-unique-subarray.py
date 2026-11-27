class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        mod1 = 10**9 + 7
        mod2 = 10**9 + 9

        base1 = 31
        base2 = 37

        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)

        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)
        for i in range(n):
            x = nums[i]

            h1[i + 1] = (h1[i] * base1 + x) % mod1
            h2[i + 1] = (h2[i] * base2 + x) % mod2

            p1[i + 1] = (p1[i] * base1) % mod1
            p2[i + 1] = (p2[i] * base2) % mod2

        def check(k):
            count = {}

            for i in range(n - k + 1):
                j = i + k

                hash1 = (h1[j] - h1[i] * p1[k]) % mod1
                hash2 = (h2[j] - h2[i] * p2[k]) % mod2

                key = (hash1, hash2)

                count[key] = count.get(key, 0) + 1

            return any(v == 1 for v in count.values())

        # Binary search
        low, high = 1, n

        while low < high:
            mid = (low + high) // 2

            if check(mid):
                high = mid
            else:
                low = mid + 1

        return low
