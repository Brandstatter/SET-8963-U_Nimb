FROM python:3.12-slim

WORKDIR /app

COPY /src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "src/main.py"]
