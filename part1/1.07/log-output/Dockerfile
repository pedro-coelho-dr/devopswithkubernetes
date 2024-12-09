FROM python:3.13-slim


COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 3000


CMD ["python", "app.py"]
