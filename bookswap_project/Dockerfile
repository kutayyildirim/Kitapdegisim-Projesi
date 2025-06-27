FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

EXPOSE 8000
# docker-compose exec web bash
# python manage.py shell
# from bookswap.tasks import send_user_list_email
# send_user_list_email.delay()
# celery -A bookswap_project worker -l info --pool=solo
# celery -A bookswap_project beat -l info