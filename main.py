def add_task(task):
    """Handles getting input and adding a new task to the list."""
    print("Adding a new item.\n")
    add_item = input("What do you want to add to your to-do list?\n").title()

    task.append(add_item)
    print(f"'{add_item}' has been added.✅")


def view_task(task):
    """Displays the to-do list in a numbered, readable format."""

    print(f"\nYou currently have {len(todo_list)} items:")
    print("---------------------------------")
    for index, item in enumerate(task):
        # index starts at 0, so we use index + 1 for the list number
        print(f"{index + 1}. {item}")


def remove_task(task):
    """Handles removing a task by number, including validation."""
    if 0 <= task_index < len(task):
        removed_item = task.pop(task_index)
        print(f"\n✅ Task '{removed_item}' has been successfully removed!")

    else:
        # If the number is outside the valid range (e.g., they enter 99)
        print(f"\n❌ Error: The number {user_number} is not on the list.")


print("----------")
print("To-Do List")
print("----------")


todo_list = []

is_running = True

while is_running:
    user_input = input(
        "Do you want to (A)dd, (R)emove, (V)iew items or (Q)uit?\nType A/R/V/Q:\n"
    ).lower()

    if user_input == "a":
        add_task(todo_list)

    elif user_input == "v":
        if todo_list == []:
            print("You have not added any items yet")
        else:
            view_task(todo_list)

    elif user_input == "q":
        print("\n--- Byeee! Come back and finish those tasks! ---")
        is_running = False

    elif user_input == "r":
        if todo_list == []:
            print("Nothing to remove! The list is empty.")
            continue

        view_task(todo_list)

        user_number = input("Enter the NUMBER of the task to remove: ")
        task_index = int(user_number) - 1

        remove_task(todo_list)

    else:
        print("\nInvalid choice. Please type 'A', 'R', 'V', or 'Q'.")
