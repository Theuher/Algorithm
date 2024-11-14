class Solution:
    def sortArray(self, nums):
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, array, low, high):
        if low >= high:
            return
        mid = low + (high - low) // 2
        self.mergeSort(array, low, mid)
        self.mergeSort(array, mid + 1, high)
        self.merge(array, low, mid, high)

    def merge(self, array, low, mid, high):
        n1 = mid - low + 1
        n2 = high - mid
        leftPart = array[low:mid + 1]
        rightPart = array[mid + 1:high + 1]

        p1 = 0
        p2 = 0
        writeInd = low

        while p1 < n1 and p2 < n2:
            if leftPart[p1] <= rightPart[p2]:
                array[writeInd] = leftPart[p1]
                p1 += 1
            else:
                array[writeInd] = rightPart[p2]
                p2 += 1
            writeInd += 1

        while p1 < n1:
            array[writeInd] = leftPart[p1]
            p1 += 1
            writeInd += 1

        while p2 < n2:
            array[writeInd] = rightPart[p2]
            p2 += 1
            writeInd += 1
