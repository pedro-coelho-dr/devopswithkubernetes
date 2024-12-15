FROM python:3.13-slim

COPY app /app/app
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD ["python", "main.py"]
