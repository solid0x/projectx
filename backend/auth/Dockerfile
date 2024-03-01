FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD python manage.py migrate && gunicorn -w 2 --bind 0.0.0.0:8000 auth.wsgi:application