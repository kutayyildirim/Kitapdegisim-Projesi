# 📚 Bookswap - Kitap Paylaşım ve Bildirim Sistemi

Bookswap, kitap severlerin birbirleriyle kitap listesi paylaşabileceği, otomatik e-posta bildirimleri alabileceği ve arka planda zamanlanmış görevlerin yürütüldüğü, Docker altyapısında çalışan bir Django projesidir.

## 🚀 Özellikler

- Kullanıcı yönetimi ve kitap paylaşımı
- Gmail tabanlı e-posta bildirimleri
- Celery & Django Celery Beat ile zamanlanmış görevler
- Redis altyapılı mesajlaşma kuyruğu
- PostgreSQL veritabanı kullanımı
- Docker ve Docker Compose uyumlu çalışma ortamı

## 🛠️ Kullanılan Teknolojiler

- Python
- Django
- Celery
- Django Celery Beat
- Redis
- PostgreSQL
- Docker & Docker Compose

## 🐳 Docker Servisleri

- **db** → PostgreSQL veritabanı
- **redis** → Redis mesajlaşma sunucusu
- **web** → Django uygulama sunucusu
- **worker** → Celery arkaplan görev yöneticisi
- **beat** → Celery zamanlayıcı servis

## 📂 Proje Yapısı

bookswap_project/
-├── bookswap/ # Django uygulaması
-├── bookswap_project/ # Proje ayarları
-├── Dockerfile
-├── docker-compose.yml
-├── requirements.txt
-├── .env

## ⏰ Zamanlanmış Görevler

Django Celery Beat sayesinde belirli aralıklarla tüm kullanıcı listesi e-posta olarak gönderilmektedir.  
Görev tanımı `bookswap/tasks.py` dosyasında bulunmaktadır.

Logları takip etmek için:

docker-compose logs -f worker
docker-compose logs -f beat


Görevi manuel tetiklemek için:

docker-compose exec web bash
python manage.py shell

Ardından:

```python
from bookswap.tasks import send_user_list_email
send_user_list_email.delay()

📧 E-Posta Bildirimleri
Uygulama, Gmail SMTP altyapısını kullanır. .env dosyasından e-posta bilgileri yönetilir. Gmail için uygulama şifresi kullanılması tavsiye edilir.
