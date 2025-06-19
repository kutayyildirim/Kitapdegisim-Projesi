# Temel Python imajı
FROM python:3.11-slim

# Ortam değişkenleri
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Çalışma dizinini oluştur
WORKDIR /app

# Gereken dosyaları kopyala
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Projeyi kopyala
COPY . /app/

# Port aç (opsiyonel, Django'nun portu)
EXPOSE 8000

# Giriş komutu
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
