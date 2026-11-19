class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        hashmap = {}
        stack = []
        for num in nums2[::-1]:
            while stack and stack[-1] < num:
                stack.pop()
            hashmap[num] = stack[-1] if stack else -1
            stack.append(num)

        ans = []
        for num in nums1:
            ans.append(hashmap[num])

        return ans
