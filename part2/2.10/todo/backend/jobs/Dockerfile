FROM python:3.13-slim

WORKDIR /app
COPY add_random_todo.py /app/add_random_todo.py

RUN pip install requests

ENV BACKEND_URL="http://todo-backend-service:5001/todos"

CMD ["python", "add_random_todo.py"]
