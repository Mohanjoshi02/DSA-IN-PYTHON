"""Practical 11A: Heap sort using a min heap or max heap."""


def heap_sort(values, heap_type="max"):
    if heap_type not in {"min", "max"}:
        raise ValueError("heap_type must be 'min' or 'max'.")
    result = list(values)
    for index in range(len(result) // 2 - 1, -1, -1):
        _sift_down(result, index, len(result), heap_type)
    for end in range(len(result) - 1, 0, -1):
        result[0], result[end] = result[end], result[0]
        _sift_down(result, 0, end, heap_type)
    return result


def _sift_down(values, root, size, heap_type):
    while True:
        child = 2 * root + 1
        if child >= size:
            return
        if child + 1 < size and _comes_before(values[child + 1], values[child], heap_type):
            child += 1
        if not _comes_before(values[child], values[root], heap_type):
            return
        values[root], values[child] = values[child], values[root]
        root = child


def _comes_before(first, second, heap_type):
    return first < second if heap_type == "min" else first > second


def main():
    values = list(map(int, input("Enter numbers separated by spaces: ").split()))
    heap_type = input("Choose heap (min/max): ").strip().lower()
    print("Sorted values:", " ".join(map(str, heap_sort(values, heap_type))))


if __name__ == "__main__":
    main()
