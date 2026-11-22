"""Practical 9B: Minimum-cost power distribution with Kruskal's algorithm."""

from practical_9a_mst_graph import kruskal


def minimum_distribution(substations, connections):
    names = {name: index for index, name in enumerate(substations)}
    indexed_connections = [
        (names[first], names[second], cost)
        for first, second, cost in connections
    ]
    tree = kruskal(len(substations), indexed_connections)
    return [
        (substations[first], substations[second], cost)
        for first, second, cost in tree
    ]


def main():
    substations = [
        name.strip()
        for name in input("Enter substation names separated by commas: ").split(",")
        if name.strip()
    ]
    connection_count = int(input("Number of possible connections: "))
    connections = []
    for _ in range(connection_count):
        first, second, cost = input(
            "Enter connection (substation1,substation2,cost): "
        ).split(",")
        connections.append((first.strip(), second.strip(), int(cost)))
    tree = minimum_distribution(substations, connections)
    print("Minimum-cost power distribution:")
    for first, second, cost in tree:
        print(f"{first} - {second}: {cost}")
    print("Minimum total cost:", sum(cost for _, _, cost in tree))


if __name__ == "__main__":
    main()
