# APlikasi Kemahasiswaan Universitas Muhammadiyah Kalimantan Timur

Aplikasi ini dibuat dengan beberapa Teknologi, Vue Js + Tailwindcss sebagai Front-end dan Django sebagai Back-end Postgresql sebagai Basis Data

Pada Repository terdapat 2 aplikasi berbeda, yaitu Vue js Dan Django, untuk menjalankannya ikuti perintah berikut

## Project Python setup (folder ./kemahasiswaan_umkt)
```
pip install -r requirements.txt
```

### Menggunakan Virtual Environment
jika ingin menggunakan Virtual Environment, maka perlu membuat Virtual Environmentnya terlebih dahulu

```
virtualenv env
```
atau
```
python -m virtualenv env
```
lalu,
```
pip install -r requirements.txt
```

### Migrasi Database

Pertama, buat database di Postgresql dengan nama "kemahasiswaan_umkt"

lalu, jalankan perintah Migrasi
```
python manage.py makemigrations
python manage.py migrate
```

### Membuat Akses Super User

Buat Akses Super User dengan username dan password bebas,
```
python manage.py createsuperuser
```

### Jalankan Program

Lalu jalankan program tsb
```
python manage.py runserver
```



## Project Vue Js setup (folder ./kemahasiswaan_umkt/templates/kemahasiswaan_umkt)

### Instalasi Vue Js
```
npm install
```

### Menjalankan Program Vue Js
```
npm run serve
```

My Name is Ricko Tiaka, hopefully we can do so much collaboration,
Support Me on Linkedin https://www.linkedin.com/in/ricko-caesar-aprilla-tiaka-191095200
Thanks for the Support
