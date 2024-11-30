## Backend Aplikasi Tugas Akhir untuk Machine Learning
Aplikasi dapat menampilkan hasil dari model yang telah dibuat (dari `model.keras`)

Aplikasi ini menggunakan FastAPI dalam pembuatan API.

Sebelum menjalankan aplikasi, pastikan seluruh dependency sudah terinstall. Anda dapat menggunakan command berikut untuk menginstal dependency:
```
pip install -r requirements.txt
```

Setelah itu, download model melalui google drive. Anda dapat menggunakan script yang sudah dibuat pada folder script:
```
python scripts/model_download.py
```

Untuk menjalankan aplikasi ini, silakan ketikkan ini di terminal anda:
```
fastapi dev main.py
```

Secara default, aplikasi akan berjalan di `localhost:8000`