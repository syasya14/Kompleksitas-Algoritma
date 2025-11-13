# Daftar nama dan skor siswa
students = [
    ("Andi", 78),
    ("Budi", 65),
    ("Citra", 85),
    ("Dewi", 72),
    ("Eka", 90)
]

# MERGE SORT berdasarkan skor siswa
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # rekursif untuk membagi
    left = merge_sort(left)
    right = merge_sort(right)

    # gabungkan (merge) dua bagian
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # bandingkan elemen kiri dan kanan berdasarkan skor
    while i < len(left) and j < len(right):
        if left[i][1] <= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # tambahkan sisa elemen
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Jalankan merge sort
sorted_students_merge = merge_sort(students)
print("\nHasil Merge Sort:")
for s in sorted_students_merge:
    print(s)