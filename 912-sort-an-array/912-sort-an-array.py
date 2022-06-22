class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
        # return self.bubbleSort(nums)
        # return self.selectionSort(nums)
        # return self.quickSort(nums)

    def quickSort(self, nums):
        # Solution Quick Sort
        # Time O(NlogN)
        # Space O(1)
        def partition(start, end):
            if start >= end:
                return

            i = start
            j = end
            pivot = end
            while i < j:
                while i < end and nums[i] < nums[pivot]:
                    i += 1
                while j >= 0 and nums[j] >= nums[pivot]:
                    j -= 1
                if i >= j: 
                    break

                nums[i], nums[j] = nums[j], nums[i]

            nums[i], nums[pivot] = nums[pivot], nums[i]

            partition(start, i-1)
            partition(i+1, end)

        partition(0, len(nums)-1)
        return nums

    def mergeSort(self, nums):
        # Solution Merge Sort
        # Time O(NlogN)
        # Space O(N)
        def mergeSortedArray(list1, list2):
            result = []
            l = 0
            r = 0
            while l < len(list1) and r < len(list2):
                if list1[l] < list2[r]:
                    result.append(list1[l])
                    l += 1
                else:
                    result.append(list2[r])
                    r += 1

            while l < len(list1):
                result.append(list1[l])
                l += 1
            while r < len(list2):
                result.append(list2[r])
                r += 1

            return result

        def partition(array):
            if len(array) <= 1:
                return array

            mid = len(array) // 2

            left = partition(array[:mid])
            right = partition(array[mid:])

            return mergeSortedArray(left, right)

        return partition(nums)

    def bubbleSort(self, nums):
        # Bubble sort
        # Time - O(N^2)
        # Space - O(1)
        for i in range(len(nums)-1):
            for j in range(0, len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums

    def selectionSort(self, nums):
        # Selection Sort
        # Time - O(N^2)
        # Space - O(1)
        for i in range(len(nums)):
            minId = i
            for j in range(i+1, len(nums)):
                if nums[minId] > nums[j]:
                    minId = j
            nums[minId], nums[i] = nums[i], nums[minId]
        return nums
    
    

    
    