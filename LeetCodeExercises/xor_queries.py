class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        n = len(arr)
        temp = [0] * n
        temp[0] = arr[0]

        results = []
        # Compute all the XOR for the arr
        # then for a given range, just Xor the right value with the previous starting value(left -1)
        for index in range(1, n):
            temp[index] = temp[index - 1] ^ arr[index]
        print(temp)

        res = []
        for left, right in queries:
            if left == 0:
                results.append(temp[right])
            else:
                results.append(temp[right] ^ temp[left - 1])

        print(results)

        return results