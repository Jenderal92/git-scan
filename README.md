# git-scan

<p>Alat ini dirancang untuk memindai dan mengidentifikasi apakah situs web memiliki direktori ".git" yang terekspos, yang bisa mengandung informasi sensitif seperti kode sumber atau file konfigurasi Git.

## Feature

<ul dir="auto">
<li>Memindai URL secara massal untuk menemukan apakah direktori ".git/HEAD" tersedia di situs web.</li>
<li>Menggunakan pustaka Python seperti "requests" untuk mengirim permintaan HTTP dan memeriksa responsnya.</li>
<li>Mendukung penggunaan multithreading untuk mempercepat proses pemindaian di banyak situs secara bersamaan.</li>
<li>Menampilkan hasil pemindaian dengan status: ditemukan (200 OK), terlarang (403 Forbidden), atau tidak ditemukan (404 Not Found).</li>
<li>Menangani kesalahan jaringan seperti timeout atau kegagalan koneksi dengan logika retry (coba ulang) yang aman.</li>
<li>Hasil yang ditemukan akan disimpan langsung ke file hasil ("results.txt") tanpa menghapus hasil sebelumnya.</li>
<li>Hasil yang ditemukan tidak akan duplikat, memastikan bahwa URL yang sama tidak disimpan lebih dari sekali.</li>
<li>Memungkinkan pengguna untuk melanjutkan pemindaian tanpa kehilangan hasil sebelumnya jika skrip dijalankan lagi.</li>
</ul>


## Buy Coffee :
<ul dir="auto">
<li>Bitcoin $: 14nXhmRiQx5joCXFTdR8ydm3T8et7MFDXC</li>
<li>Saweria $: https://saweria.co/Shin403</li>
<li>Trakteer $: https://trakteer.id/shin403</li>
<li>Buymeacoffee $: https://www.buymeacoffee.com/shin.code</li>
<li>Ko-Fi $: https://ko-fi.com/shincode403</li>
</ul>

![Jenderal92 Git Scanner](https://github.com/user-attachments/assets/bb7c8a3a-d39e-44f8-b623-2010ce5bded8)


## How To Run?
<ul dir="auto">
<li>Install Python by downloading it from the official Python website <a href="https://www.python.org">https://www.python.org</a>.</li>
<li> Install module <code>pip install requests beautifulsoup4 colorama</code></li>
<li><code>python file.py</code></li>
<li>Put ur list sites (e.g., url.txt)</li>
</ul>

## Disclaimer !!!

<p>I have written the disclaimer on the cover of Jenderal92. You can check it <a href="https://github.com/Jenderal92">HERE !!!</a></p>
