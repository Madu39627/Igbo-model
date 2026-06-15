FROM python:3.10

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY models ./models

EXPOSE 5002

ENV FLASK_APP=app.py
ENV FLASK_RUN_PORT=5002
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]