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

if __name__ == "__main__":
    app = App()

    arr = [132, 3, 4, 1, 45, 5, 64, 62]

    app.merge_sort(arr, 0, len(arr) - 1)

    print(arr)

    print("max:", app.find_max(arr, 0, len(arr) - 1))
    print(app.binary_search(arr, 0, len(arr) - 1, 5))