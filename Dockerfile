FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBUG=False \
    ALLOWED_HOSTS=localhost,127.0.0.1,[::1]

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput \
    && python manage.py migrate --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
