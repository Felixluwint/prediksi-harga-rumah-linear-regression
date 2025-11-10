FROM python:3.10-slim

WORKDIR /app

COPY backend /app

RUN pip install --no-cache-dir -r backend/requirements.txt

CMD ["python", "app.py"]

EXPOSE 5000
