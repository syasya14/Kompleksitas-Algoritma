# QUICK SORT berdasarkan skor siswa
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # gunakan elemen terakhir sebagai pivot
    pivot = arr[-1]

    left = []
    right = []

    # bandingkan berdasarkan skor (elemen ke-1 dari tuple)
    for x in arr[:-1]:
        if x[1] <= pivot[1]:
            left.append(x)
        else:
            right.append(x)

    # gabungkan hasil rekursif
    return quick_sort(left) + [pivot] + quick_sort(right)


# Data siswa
students = [
    ("Andi", 78),
    ("Budi", 65),
    ("Citra", 85),
    ("Dewi", 72),
    ("Eka", 90)
]

# Jalankan quick sort
sorted_students_quick = quick_sort(students)
print("Hasil Quick Sort:")
for s in sorted_students_quick:
    print(s)