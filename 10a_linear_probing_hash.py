"""Practical 10A: Hashing with linear probing, with or without replacement."""


class LinearProbingHashTable:
    def __init__(self, size, replace=False):
        if size <= 0:
            raise ValueError("Table size must be positive.")
        self.table = [None] * size
        self.replace = replace

    def _index(self, key):
        return key % len(self.table)

    def insert(self, key, value):
        index = self._index(key)
        for position, item in enumerate(self.table):
            if item is not None and item[0] == key:
                self.table[position] = (key, value)
                return position
        if self.replace and self.table[index] is not None:
            occupant = self.table[index]
            if self._index(occupant[0]) != index:
                self.table[index] = (key, value)
                return self._insert_from((index + 1) % len(self.table), occupant)
        return self._insert_from(index, (key, value))

    def _insert_from(self, start, entry):
        for offset in range(len(self.table)):
            position = (start + offset) % len(self.table)
            if self.table[position] is None:
                self.table[position] = entry
                return position
        raise OverflowError("Hash table is full.")

    def display(self):
        for index, item in enumerate(self.table):
            print(f"{index}: {item if item is not None else 'Empty'}")


def main():
    size = int(input("Hash table size: "))
    replace = input("Use replacement? (y/n): ").strip().lower() == "y"
    table = LinearProbingHashTable(size, replace)
    count = int(input("Number of records: "))
    for _ in range(count):
        key, value = input("Enter key and value: ").split(maxsplit=1)
        table.insert(int(key), value)
    table.display()


if __name__ == "__main__":
    main()
