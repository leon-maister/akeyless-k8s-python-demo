FROM python:3.12-alpine

WORKDIR /app

COPY get_akeyless_secret.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "get_akeyless_secret.py"]
