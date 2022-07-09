class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
        # return self.bubbleSort(nums)
        # return self.selectionSort(nums)
        # return self.quickSort(nums)
        # return self.countingSort(nums)
        # return self.radixSort(nums)
        # return self.insertionSort(nums)
        # return self.bucketSort(nums)
        
    def bucketSort(self, nums):
        if len(nums) == 0:
            return nums
        
        nofBuckets = 10
        nmsMin = min(nums)
        nmsMax = max(nums)
        rnge = (nmsMax - nmsMin) / nofBuckets
        
        buckets = []
        for i in range(nofBuckets):
            buckets.append([])
            
        for i in range(len(nums)):
            diff = (nums[i] - nmsMin) / rnge - int((nums[i] - nmsMin) / rnge)
            
            if(diff == 0 and nums[i] != nmsMin):
                buckets[int((nums[i] - nmsMin) / rnge) - 1].append(nums[i])
            else:
                buckets[int((nums[i] - nmsMin) / rnge)].append(nums[i])
        
        result = []
        for i in range(len(buckets)):
            if len(buckets[i]) != 0:
                buckets[i].sort()
                result = result + buckets[i] 
            
        return result
    
    def insertionSort(self, nums):
        # Solution - Insertion Sort
        # Time - O(N^2)
        # Space O(1)
        for i in range(1, len(nums)):
            j = i - 1
            while j >= 0 and nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                j -= 1
        
        return nums
    
    def radixSort(self, nums):
        # Solution - Radix sort
        # Time - O(log(max(N)) * ( R + N ) ) 
        #     R -> range of input
        #     N -> array
        # Space - (R + N)
        def countingSortByDigit(nums, digit):
            div = pow(10, digit)
            result = [0] * len(nums)
            rangeArray = [0] * (max(nums) + 1)
            
            for i in range(len(nums)):
                d = math.trunc(nums[i] / div) % 10 
                rangeArray[d] += 1
            
            for i in range(1, len(rangeArray)):
                rangeArray[i] = rangeArray[i-1] + rangeArray[i]
            
            for i in range(len(nums) -1, -1 ,-1):
                d = math.trunc(nums[i] / div) % 10
                idx = rangeArray[d]
                result[idx - 1] = nums[i]
                rangeArray[d] -= 1
            
            return result 
            
        
        maxinList = max(nums)
        # count nof digits
        digitCount = 0
        while maxinList != 0:
            digitCount += 1
            maxinList = math.trunc(maxinList / 10)
        
        for i in range(digitCount):
            nums = countingSortByDigit(nums, i)
            
        return nums
        
        

    def countingSort(self, nums):
        # Solution Counting sort
        # Time - O(N)
        # Space O(max(N))
        result = [0] * len(nums)
        freq = [0] * (max(nums) + 1)
        
        for i in range(len(nums)):
            freq[nums[i]] += 1
        
        for i in range(1, len(freq)):
            freq[i] = freq[i] + freq[i-1]
        
        for i in range(len(nums) - 1, -1, -1):
            idx = freq[nums[i]]
            result[idx-1] = nums[i]
            freq[nums[i]] -= 1
        
        return result
        
    def quickSort1(self, nums):
        # Solution Quick Sort - using dutch flag
        # Time O(NlogN)
        # Space O(1)
        def partition(start, end):
            if start >= end:
                return

            i = start - 1
            j = start
            pivot = end
            while j < end:
                if nums[j] < nums[pivot]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
                else: 
                    j += 1
            
            nums[i+1], nums[pivot] = nums[pivot], nums[i+1]
            
            partition(start, i)
            partition(i+2, end)

        partition(0, len(nums)-1)
        return nums

    def quickSort(self, nums):
        # Solution Quick Sort
        # Time O(NlogN)
        # Space O(1)
        def partition(start, end):
            if start >= end:
                return

            i = start - 1
            j = start
            pivot = end
            while j < end:
                if nums[j] < nums[pivot]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
                else: 
                    j += 1
            
            nums[i+1], nums[pivot] = nums[pivot], nums[i+1]
            
            partition(start, i)
            partition(i+2, end)

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
    
    

    
    