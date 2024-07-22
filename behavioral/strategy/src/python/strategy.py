from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, array):
        pass

class QuickSortStrategy(SortStrategy):
    def sort(self, array):
        self.quick_sort(array, 0, len(array) - 1)
    
    def quick_sort(self, array, low, high):
        if low < high:
            pi = self.partition(array, low, high)
            self.quick_sort(array, low, pi - 1)
            self.quick_sort(array, pi + 1, high)
    
    def partition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

class BubbleSortStrategy(SortStrategy):
    def sort(self, array):
        n = len(array)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]

class MergeSortStrategy(SortStrategy):
    def sort(self, array):
        self.merge_sort(array, 0, len(array) - 1)
    
    def merge_sort(self, array, left, right):
        if left < right:
            middle = (left + right) // 2
            self.merge_sort(array, left, middle)
            self.merge_sort(array, middle + 1, right)
            self.merge(array, left, middle, right)
    
    def merge(self, array, left, middle, right):
        n1 = middle - left + 1
        n2 = right - middle

        L = array[left:left + n1]
        R = array[middle + 1:middle + 1 + n2]

        i = j = k = 0

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            array[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            array[k] = R[j]
            j += 1
            k += 1


class DataProcessor:
    def __init__(self, sort_strategy):
        self.sort_strategy = sort_strategy

    def set_sort_strategy(self, sort_strategy):
        self.sort_strategy = sort_strategy

    def process_data(self, data):
        self.sort_strategy.sort(data)
        # Further processing after sorting
        return data

def main():
    data_processor = DataProcessor(QuickSortStrategy())

    data = [5, 2, 9, 1, 5, 6]

    # Using QuickSort
    data_processor.process_data(data)
    print("QuickSort:", data)

    # Using BubbleSort
    data = [5, 2, 9, 1, 5, 6]
    data_processor.set_sort_strategy(BubbleSortStrategy())
    data_processor.process_data(data)
    print("BubbleSort:", data)

    # Using MergeSort
    data = [5, 2, 9, 1, 5, 6]
    data_processor.set_sort_strategy(MergeSortStrategy())
    data_processor.process_data(data)
    print("MergeSort:", data)

def print_array(array):
    print(" ".join(map(str, array)))

if __name__ == "__main__":
    main()
