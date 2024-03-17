class Solution:
    # Decent solution with time limited excced problem
    #
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        nums = list(set(nums))
        if len(nums) == 1:
            return True
        nums = sorted(nums)
        max_num = nums[-1]
        all_prime = []

        def is_prime(x):
            if x == 1:
                return False
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True

        for i in range(1, max_num + 1):
            if is_prime(i):
                all_prime.append(i)

        def get_uni_prime(x, list_prime):
            result = set()
            for prime in list_prime:
                while x % prime == 0:
                    x = x // prime
                    if prime not in result:
                        result.add(prime)
            return result

        vertex = {}
        for num in nums:
            if num == 1:
                return False
            uniq_prime = get_uni_prime(num, all_prime)
            if uniq_prime:
                vertex[num] = uniq_prime
        # collasing componenet
        components = []
        for v, set_prime in vertex.items():
            found = False
            if not components:
                components.append(set_prime)
            else:
                for i in range(len(components)):
                    _com = components[i]
                    if _com.intersection(set_prime):
                        components[i] = _com.union(set_prime)
                        found = True
                if not found:
                    components.append(set_prime)
                delete_id = []
                for i in range(1, len(components)):
                    if components[i].intersection(components[i - 1]):
                        components[i] = components[i].union(components[i - 1])
                        delete_id.append(i - 1)
                for id in delete_id:
                    del components[id]

        if len(components) > 1:
            for i in range(1, len(components)):
                if not components[i].intersection(components[i - 1]):
                    return False
        if not components:
            return False
        return True


# Accepted solution
