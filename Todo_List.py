import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.input_frame, width=40)
        self.task_entry.grid(row=0, column=0, padx=5)

        self.add_button = tk.Button(self.input_frame, text="Add", command=self.add_task)
        self.add_button.grid(row=0, column=1)

        self.task_listbox = tk.Listbox(self.root, width=50, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.action_frame = tk.Frame(self.root)
        self.action_frame.pack(pady=10)

        self.complete_button = tk.Button(self.action_frame, text="Mark Done", command=self.mark_completed)
        self.complete_button.grid(row=0, column=0, padx=5)

        self.delete_button = tk.Button(self.action_frame, text="Remove", command=self.delete_task)
        self.delete_button.grid(row=0, column=1, padx=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append({"name": task, "completed": False})
            self.task_entry.delete(0, tk.END)
            self.refresh_tasks()
        else:
            messagebox.showwarning("Error", "Please enter a task.")

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task["completed"] else "✗"
            self.task_listbox.insert(tk.END, f"{status} {task['name']}")

    def mark_completed(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = True
            self.refresh_tasks()
        else:
            messagebox.showwarning("Error", "No task selected.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.refresh_tasks()
        else:
            messagebox.showwarning("Error", "No task selected.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
