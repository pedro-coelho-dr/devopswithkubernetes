import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://todo-backend-service:5001/todos")

def fetch_random_wikipedia_url():
    response = requests.get("https://en.wikipedia.org/wiki/Special:Random", allow_redirects=False)
    location = response.headers.get("Location")
    if location:
        return location
    return None

def post_todo(todo_content):
    response = requests.post(BACKEND_URL, json={"todo": todo_content})
    if response.status_code == 201:
        print(f"Successfully added todo: {todo_content}")
    else:
        print(f"Failed to add todo. Response: {response.status_code}, {response.text}")

if __name__ == "__main__":
    wikipedia_url = fetch_random_wikipedia_url()
    if wikipedia_url:
        todo_message = f"Read {wikipedia_url}"
        post_todo(todo_message)
    else:
        print("Failed to fetch Wikipedia URL.")
