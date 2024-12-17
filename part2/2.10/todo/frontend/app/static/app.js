// Function to refresh the TODO list
async function refreshTodoList() {
    const response = await fetch("/todo");
    const html = await response.text();
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, "text/html");
    const newTodoList = doc.querySelector(".todo-list");
    document.querySelector(".todo-list").innerHTML = newTodoList.innerHTML;
}

async function addTodo(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const response = await fetch("/add-todo", {
        method: "POST",
        body: formData
    });

    const result = await response.json();
    const messageContainer = document.getElementById("message");

    if (response.ok) {
        messageContainer.textContent = "✅ " + result.message;
        messageContainer.style.color = "green";
        event.target.reset();
        await refreshTodoList();
    } else {
        messageContainer.textContent = "❌ " + result.error;
        messageContainer.style.color = "red";
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const todoForm = document.querySelector("form");
    if (todoForm) {
        todoForm.addEventListener("submit", addTodo);
    }
});
