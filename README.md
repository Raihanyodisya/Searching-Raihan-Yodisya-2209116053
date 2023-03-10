Nama : Raihan Yodisya 
NIM : 2209116053
Kelas : Sistem Informasi (B)

"ALGORITMA SEARCHING"

Algoritma searching adalah suatu program yang ada pada python untuk mencari suatu data.
Algoritma ini berfungsi untuk menemukan nilai atau indeks tertentu dalam sekumpulan data yang
tipenya sama. Hasil akhir algoritma searching pada umumnya adalah akan mendapatkan dua
kemungkinan. Pertama, data berhasil ditemukan atau kedua yaitu sebaliknya gagal dalam menemukan
suatu data yang dicari. 

Sebenarnya algoritma searching / pencarian sangat banyak jenisnya. Ada dua algoritma yang
diajarkan pada praktikum ASD ini. pertama ada "Fibonacci Search" dan kedua ada "Jump search".
Untuk Fibonacci search sendiri adalah suatu algoritma yang mana menerapkan prinsip bilangan
Fibonacci. Dalam ilmu komputer, algoritma ini menggunakan konsep divide  dan conquer. Fibonacci
search hanya memeriksa lokasi yang yang memiliki tingkat penyebaran data yang rendah. Fibbonaci
search dalam prakteknya memiliki keuntungan yakni cepatnya mengakses data pada suatu storage.

Sedangkan Jump search merupakan merupakan metode searching untuk data yang terurut. Jump search
digunakan untuk mengurangi pengecekan data seperti linear search dimana jump search menggunakan
metode lompat secara teratur untuk menemukan data yang dicari.

Dan pada kesempatan kali ini ada sebuah soal yang mengharuskan untuk mencari sebuah Index yaitu seperti berikut ini : 
var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

Buatlah sebuah program python yang dapat mencari data-data yang sudah di sediakan dengan output
1. Arsel di Index 0, Avivah di Index 1, Daiva di Index 2
2. Wahyu di Index 3 pada kolom 0
3. Wibi di Index 3 pada kolom 1

Disini saya menggunakan Algoritma Searching "Jump Search & Linear Search"


"Linear Search"

Linear search adalah program pencarian yang mudah dipahami, linear search memiliki kelebihan
apabila data yang di cari letaknya pada data – data awal sehingga prosesnya berjalan cepat,
namun apabila data yang di cari letaknya pada data terakhir maka pencarian lebih memakan waktu
yang cukup lama pula. karena di linear search mengunjungi setiap elemen data yang ada.

Disini linear search digunakan dengan bisa menginput nama yang ingin kita ketahui berada di
index mana dan pada kolom berapa. Dengan menginput nama yang sesuai maka akan bisa untuk
menemukan index maupun nama pada kolom dan jika salah input nama maka akan muncul keterangan
berupa "Nama Tidak Ditemukan". Penggunaannya pun juga cukup mudah hanya perlu input salah satu
nama dan akan keluar hasilnya.
![linear-search](https://user-images.githubusercontent.com/126870046/224344996-02b63cfd-ff74-4a86-b373-84e17704da01.png)


"Jump Search"

Jump search adalah algoritma pencarian untuk yang diurutkan. Ide dasarnya adalah untuk memeriksa lebih sedikit elemen (dari pencarian linier) dengan melompat maju dengan langkah - langkah tetap atau melewatkan beberapa elemen untuk mencari semua elemen. 

Contohnya adalah semisal kita mempunyai array. array[] ukuran n dan blok (untuk dilompati) ukuran m. Setelah itu kita mencari di arr indeks[0], arrr[m], arr[2m] sampai ar[km] dan seterusnya. Setelah menemukan interval (arr[km] <x <arr[(k + 1) m]), dilakukan operasi pencarian linear dari indeks km untuk menemukan elemen x (Nayal,2016).
![maxresdefault](https://user-images.githubusercontent.com/126870046/224341961-76f036c6-4093-4e97-8327-a46e036e98a6.jpg)
