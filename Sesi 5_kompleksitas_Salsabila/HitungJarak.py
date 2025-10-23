# === Import Library ===
from itertools import permutations

# === Data Kota dan Jarak ===
cities = ['A', 'B', 'C', 'D', 'E']
distance = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 15],
    [25, 30, 20, 15, 0],
]

# === Fungsi Menghitung Total Jarak ===
def route_distance(route):
    total = 0
    for i in range(len(route) - 1):
        total += distance[route[i]][route[i + 1]]
    total += distance[route[-1]][route[0]]
    return total

# === Mulai dari Kota A ===
start = 0
other_indices = [1, 2, 3, 4]

results = []

# === Coba Semua Rute ===
for perm in permutations(other_indices):
    route = [start] + list(perm)
    total = route_distance(route)
    results.append((route, total))

# === Cari Rute Terpendek ===
min_distance = min(total for (_, total) in results)
best_routes = [route for (route, total) in results if total == min_distance]

# === Cetak Semua Rute ===
print("Semua rute dan total jaraknya:\n")
for route, total in results:
    route_names = [cities[i] for i in route] + [cities[route[0]]]
    print(f"{' -> '.join(route_names)} = {total}")

# === Cetak Rute Terpendek ===
print("\nRute terpendek:")
for route in best_routes:
    route_names = [cities[i] for i in route] + [cities[route[0]]]
    print(f"{' -> '.join(route_names)} = {min_distance}")