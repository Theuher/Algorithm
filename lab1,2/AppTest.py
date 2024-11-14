import unittest
import ast

class App:
    def insertion_sort(self, arr):
        for j in range(1, len(arr)):
            key = arr[j]
            i = j - 1
            while i >= 0 and arr[i] > key:
                arr[i + 1] = arr[i]
                i -= 1
            arr[i + 1] = key
        return arr

    def find_max(self, arr, l, r):
        if l == r:
            return arr[l]
        mid = (l + r) // 2

        max_left = self.find_max(arr, l, mid)
        max_right = self.find_max(arr, mid + 1, r)

        return max(max_left, max_right)

    def merge_sort(self, arr, p, r):
        if p < r:
            q = (p + r) // 2
            self.merge_sort(arr, p, q)
            self.merge_sort(arr, q + 1, r)
            self.merge(arr, p, q, r)

    def merge(self, arr, p, q, r):
        n1 = q - p + 1
        n2 = r - q

        left = arr[p:p + n1]
        right = arr[q + 1:q + 1 + n2]

        i = j = 0
        k = p

        while i < n1 and j < n2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = left[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = right[j]
            j += 1
            k += 1

    def binary_search(self, arr, min_index, max_index, key):
        if min_index > max_index:
            return -1
        mid = (min_index + max_index) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return self.binary_search(arr, mid + 1, max_index, key)
        else:
            return self.binary_search(arr, min_index, mid - 1, key)

class TestApp(unittest.TestCase):

    def parse_array_from_string(self, line):
        parts = line.strip().split(", ")
        return [int(x) for x in parts]

    def test_insertion_sort(self):
        app = App()

        with open("sortTestCase.txt") as f:
            line = f.readline()
            tokens = line.split(":")
            unsorted_array = self.parse_array_from_string(tokens[0])
            expected_sorted_array = self.parse_array_from_string(tokens[1])

            sorted_array = app.insertion_sort(unsorted_array)

            self.assertEqual(expected_sorted_array, sorted_array)

    def test_merge_sort(self):
        app = App()

        with open("sortTestCase.txt") as f:
            line = f.readline()
            tokens = line.split(":")
            unsorted_array = self.parse_array_from_string(tokens[0])
            expected_sorted_array = self.parse_array_from_string(tokens[1])

            app.merge_sort(unsorted_array, 0, len(unsorted_array) - 1)

            self.assertEqual(expected_sorted_array, unsorted_array)

    def test_binary_search(self):
        app = App()

        with open("binarySearchTestCase.txt") as f:
            line = f.readline()
            tokens = line.split(":")
            arr = self.parse_array_from_string(tokens[0])
            key = int(tokens[1])
            expected_index = int(tokens[2])

            index = app.binary_search(arr, 0, len(arr) - 1, key)

            self.assertEqual(expected_index, index)

    def test_find_max(self):
        app = App()

        with open("findMaxTestCase.txt") as f:
            line = f.readline()
            tokens = line.split(":")
            arr = self.parse_array_from_string(tokens[0])
            expected_max = int(tokens[1])

            max_value = app.find_max(arr, 0, len(arr) - 1)

            self.assertEqual(expected_max, max_value)

if __name__ == "__main__":
    unittest.main()