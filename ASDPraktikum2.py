#"Linear Search"

var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

print(f"1. {var[0]} di Index 0, {var[1]} di Index 1, {var[2]} di Index 2")
print(f"2. {var[3][0]} di Index 3 pada kolom 0")
print(f"3. {var[3][1]} di Index 3 pada kolom 1")

def linear_search(name, lst):
    for i in range(len(lst)):
        if name == lst[i]:
            return i
        elif type(lst[i]) == list:
            result = linear_search(name, lst[i])
            if result != -1:
                return (i, result)
    return -1

nama = input("Masukkan Nama Yang Ingin Dicari : ")
result = linear_search(nama, var)
if result == -1:
    print("Nama Tidak Ditemukan")
else:
    if type(result) == int:
        print(f"Index dari {nama} adalah {result}")
    else:
        print(f"Index dari {nama} adalah {result[0]} pada kolom {result[1]}")

import math

#"Jump Search"

nama = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

def jump_search(arr, x):
    lenght = len(arr)
    jump = int(math.sqrt(lenght))
    left, right = 0, 0
    while left < lenght and arr[left] <= x:
        right = min(lenght- 1, left + jump)
        if arr[left] <= x and arr[right] >= x:
            break
        left += jump
    if left >= lenght or arr[left] > x:
        return -1
    right = min(lenght - 1, right)
    i = left
    while i <= right and arr[i] <= x:
        if arr[i] == x:
            return i
        i += 1
    return -1

idx_arsel = jump_search(nama, "Arsel")
if idx_arsel != -1:
    print("Arsel berada Index", idx_arsel)
else:
    print("Arsel tidak Ada")

#Search Avivah
idx_avivah = jump_search(nama, "Avivah")
if idx_avivah != -1:
    print("Avivah berada Index", idx_avivah)
else:
    print("Avivah tidak Ada")

#Search Daiva
idx_daiva = jump_search(nama, "Daiva")
if idx_daiva != -1:
    print("Daiva berada Index", idx_daiva)
else:
    print("Daiva tidak Ada")

#Search Wahyu
idx_wahyu = jump_search(nama[3], "Wahyu")
if idx_wahyu != -1:
    print("Wahyu berada pada Index 3 di kolom 0")
else:
    print("Wahyu tidak Ada")

#Search Wibi
idx_wibi = jump_search(nama[3], "Wibi")
if idx_wibi != -1:
    print("Wibi berada pada Index 3 di kolom 1")
else:
    print("Wibi tidak Ada")