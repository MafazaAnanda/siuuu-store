*Link Aplikasi: https://mafaza-ananda-footballnews.pbp.cs.ui.ac.id/

*Langkah-langkah implementasi
1. Membuat sebuah proyek Django baru
   -Membuat folder baru untuk projek ini
   -Membuat dan mengaktifkan virtual enviroment
   -Menyiapkan dependecies yaitu requirements.txt dan dan menginstallnya
   -Start project dengan nama siuuu-store sesuai dengan nama toko untuk projek saya
   -Mengkonfigurasi environment variables 
   -Memodifikasi settings.py dengan menambahkan load_dotenv(), "127.0.0.1" pada ALLOWED_HOSTS, PRODUCTION, serta mengubah databases seperti pada tutorial 0 
2. Membuat aplikasi dengan nama main pada proyek tersebut
   -Startapp dengan nama main untuk aplikasi ini dan menambahkan main ke installed_apps yang ada di settings.py
3.  Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
    -Menambahkan path('', include('main.urls')) pada urls.py yang ada di folder siuuu-store
4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib
    -Memasukkan atribut-atribut yang wajib ke dalam manage.py
5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    -Membuat folder templates pada main, lalu tambahkan file main.html
    -Membuat fungsi show_main yang di mana digunakan untuk merender main.html
    -Memodifikasi html.main agar dapat menampilkan data yang diinginkan
6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
    -Membuat file urls.py pada folder main yang berisi konfigurasi routing untuk aplikasi
7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    -Membuat repositori baru di git dengan nama siuuu-store
    -Menghubungkan proyek dengan repo tersebut
    -Membuat proyek baru di PWS dengan nama siuuustore
    -Memodifikasi project environment variables sesuai dengan data saya
    -Menanmbahkan URL dari deployment PWS ke ALLOWED_HOSTS
    -Menghubungkan proyek dengan PWS
    -Deploy proyek 

*Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Link bagan: ristek.link/Django_request_response
1. Client browser mengirim sebuah http request lalu urls.py akan menerimanya dan mencocokan dengan url pattern yang ada.
2. Jika ada yang cocok, maka akan menjalankan fungsi view yang sesuai
3. views.py akan menerima requenstnya lalu akan memprosesnya
4. views.py akan meminta data dari models.py yang di mana akan diproses lalu dikembalikan lagi ke views.py 
5. views.py akan mengirim data ke file html lalu akan dirender dan baru dikembalikan ke views.py
6. views.py akan memberikan response berupa page html kepada client browser

*Jelaskan peran settings.py dalam proyek Django!
Sebagai pusat konfigurasi untuk Django

*Bagaimana cara kerja migrasi database di Django?
-Menggunakan command python manage.py makemigrations untuk membuat file migrasi berdasarkan model yang ada di models.py
-Menggunakan command python manage.py migrate untuk mengeksekusi file migrasi yang tadi telah dibuat

*Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Karena simpel dan mudah diaplikasikan

*Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Asisten dosen sudah menyampaikan informasi-informasi yang diperlukan untuk menyelesaikan tutorial 1