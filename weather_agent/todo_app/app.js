function addTodo() {
    const todoInput = document.getElementById("todo-input");
    const todoText = todoInput.value.trim();

    if (todoText.length > 0) {
        const todoList = document.getElementById("todo-list");
        const listItem = document.createElement("li");
        listItem.textContent = todoText;
        todoList.appendChild(listItem);

        todoInput.value = "";
    }
}
