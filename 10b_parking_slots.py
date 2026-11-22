"""Practical 10B: Parking-slot allocation using linear probing."""

from practical_10a_linear_probing_hash import LinearProbingHashTable


def allocate_slots(vehicle_numbers, slot_count):
    table = LinearProbingHashTable(slot_count)
    allocations = {}
    for vehicle in vehicle_numbers:
        slot = table.insert(vehicle, vehicle)
        allocations[vehicle] = slot
    return allocations


def main():
    slot_count = int(input("Number of parking slots: "))
    vehicle_count = int(input("Number of vehicles: "))
    vehicles = [
        int(input(f"Vehicle {number} registration number: "))
        for number in range(1, vehicle_count + 1)
    ]
    allocations = allocate_slots(vehicles, slot_count)
    for vehicle, slot in allocations.items():
        print(f"Vehicle {vehicle} -> Slot {slot}")


if __name__ == "__main__":
    main()
