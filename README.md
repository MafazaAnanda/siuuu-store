*Link Aplikasi: https://pbp.cs.ui.ac.id/mafaza.ananda/siuuustore
*TUGAS 2

*Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
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

*TUGAS 3

*Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Karena data delivery berguna agar platform dapat bekerja dengan akurat, di mana format yang diberikan haruslah konsisten.

*Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya JSON lebih baik daripada karena bagi saya lebih mudah untuk dibaca. Alasan JSON lebih populer dibandingkan XML adalah karena JSON lebih cepat untuk di-parse dan lebih compact dibandingkan XML. Alasan ini saya dapatkan dari link sebagai berikut: https://www.w3schools.com/js/js_json_xml.asp & https://stackoverflow.com/questions/5615352/xml-and-json-advantages-and-disadv

*Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Untuk mengecek apakah form yang diisi sudah sesuai dengan requirementnya. is_valid() dibutuhkan karena kita ingin form yang diisi sesuai dengan requirement yang kita berikan.

*Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token dibutuhkan karena berfungsi sebagai pencegah Cross Site Request Forgery di mana akan digenerate sebuah token. Jika kita menggunakan csrf_token ini, maka akan rentan terhadap serangan CSRF tadi. Para penyerang bisa saja masuk ke browser korban yang sedang login lalu mengirim request yang berbahaya seperti transfer uang dll.

*Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat skeleton untuk kerangka views
    -Membuat folder templates di main folder lalu membuat file base.html
    -Update templates yang ada di settings.py dan juga main.html yang di mana nanti akan digunakan untuk menampilkan halaman main
2. Membuat form input dan display
    -Membuat file forms.py di main dan menambahkan class itemsform yang berisi apa saja yang perlu di input di form
    -Update views.py agar bisa menampilkan halaman untuk add item dan juga detail dari itemnya
    -Menambahkan url pattern di folder main agar bisa menampilkan halaman add item dan detail dari item
    -Membuat 2 file html, yaitu add_item dan item_detail
3. Menambahkan 4 fungsi, yaitu show_xml, show_json, show_xml_by_id, dan show_json_by_id
    - Buat 4 fungsi ini di views.py lalu routing juga urlnya
       
*Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Asisten dosen sudah memberikan tutorial berupa live coding sebelum memulai tutorial dan sangat membantu.

*Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md
Link: https://drive.google.com/drive/folders/1AnnbCUxVTXdxXLghML9VaGUMKOIDB8EI?hl=id

*Tugas 4

*Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
Class bawaan dari Django yang berfungsi untuk menangani proses autentikasi berupa login dari user yang mena menyediakan validadi dari username dan password yang ditulis user.
Kelebihan:
    -Mudah untuk digunakan
    -Aman digunakan termasuk aman dari serangan CSRF
    -Handle error yang jelas
Kekurangan:
    -Lumayan susah untuk dikustomisasi

*Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut? 
Autentikasi lebih kepada verifikasi siapa yang ingin login sedangkan otorisasi lebih kepada pemberian akses terhadap orang yang sudah terautentikasi.
Autentikasi ditangani oleh sistem login/logout dan User model bawaan. Sedangkan otorisasi ditangani oleh sistem permissions dan groups di mana sudah disediakan izin bawaan seperti add, change, delete, dan view di setiap model.

*Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Session:
    Kelebihan:
        -Lebih aman
        -Ukurannya besar
    Kelemahan:
        -Beban server yang tinggi
Cookies:
    Kelebihan:
        -Simpel
        -persisten
    Kekurangan   
        -Kurang aman
        -Ukurannya kecil                                                          

*Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Cookies secara default belum aman, masih bisa terkena serangan seperti CSRF. Django membuat token CSRF di form POST untuk mencegah penyerangan.

*Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat form registrasi dan login logout
    -Membuat fungsi registrasi di views.py, lalu buat register.html untuk page register, dan routing urlnya
    -Membuat fungsi login dan logout di views.py, lalu buat login.html untuk page login, dan routing kedua urlnya.
    -Restriksi tampilan main dan detail item agar harus login 
2. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
    -Update fungsi login_user dan show_main untuk menambahkan cookie baru lalu menampilkannya
    -Update fungsi logout_user agar bisa menghapus cookie last_login
3. Menghubungkan model dengan user
    -Update class item pada models.py agar item-item yang sudah ditambahkan sebelumnya tetap valid dan menghapus item jika user dihapus
    -update show_main agar menampilkan username dengan user yang sedang login sekarang, lalu tambahkan filter my dan all untuk main.html agar bisa bisa memfilter itemnya berdasarkan orang yang menambahkan itemnya
4. Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.
    -2 akun dengan akun pertama usernamenya Faza, dan akun kedua Paja, di mana untuk 3 item Faza adalah Nike Skills Total 90, Nike Grip3, dan Predator Elite Fold-Over Tongue Firm Ground Boots, sedangkan untuk 3 item Paja adalah Real Madrid 25/26 Third Jersey Replica, Brazil 2004 Total 90 Reissue, dan Portugal 25 Home Jersey Replica.