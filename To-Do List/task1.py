import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import os

class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Title: {self.title}, Due: {self.due_date}, Priority: {self.priority}, Status: {status}"

# Initialize the global tasks list
tasks = []

def get_task_color(task):
    """Determine the background color based on task priority and completion status."""
    if task.completed:
        return '#d0f0c0'  # Light green for completed tasks
    if task.priority == 'high':
        return '#ff6666'  # Light red for high priority tasks
    elif task.priority == 'medium':
        return '#ffcc66'  # Light yellow for medium priority tasks
    elif task.priority == 'low':
        return '#66ccff'  # Light cyan for low priority tasks
    return '#ffffff'  # Default white for tasks with no priority

def animate_task_completion(listbox, index):
    """Animate the color change for a completed task."""
    def animate_step(step=0):
        color = f'#{int(255 - step * (255 - 208))}{int(255 - step * (255 - 240))}{int(255 - step * (255 - 192))}'
        listbox.itemconfig(index, {'bg': color})
        if step < 10:
            app.after(50, animate_step, step + 1)
        else:
            listbox.itemconfig(index, {'bg': '#d0f0c0'})  # Final color

    animate_step()

def add_task():
    """Open a dialog to add a new task."""
    def save_task(event=None):
        title = title_entry.get()
        description = description_entry.get()
        due_date = due_date_entry.get()
        priority = priority_combobox.get().lower()
        
        if priority not in ['low', 'medium', 'high']:
            messagebox.showerror("Error", "Priority must be 'low', 'medium', or 'high'.")
            return
        
        task = Task(title, description, due_date, priority)
        tasks.append(task)
        update_task_list()
        add_task_window.destroy()

    def cancel_task():
        """Close the popup without saving."""
        add_task_window.destroy()

    # Create a new window for adding tasks
    add_task_window = tk.Toplevel(app)
    add_task_window.title("Add New Task")
    add_task_window.geometry("300x250")

    tk.Label(add_task_window, text="Title:").pack(pady=5)
    title_entry = tk.Entry(add_task_window, width=40)
    title_entry.pack(pady=5)

    tk.Label(add_task_window, text="Description:").pack(pady=5)
    description_entry = tk.Entry(add_task_window, width=40)
    description_entry.pack(pady=5)

    tk.Label(add_task_window, text="Due Date:").pack(pady=5)
    due_date_entry = tk.Entry(add_task_window, width=40)
    due_date_entry.pack(pady=5)

    tk.Label(add_task_window, text="Priority:").pack(pady=5)
    priority_combobox = ttk.Combobox(add_task_window, values=['Low', 'Medium', 'High'])
    priority_combobox.pack(pady=5)
    priority_combobox.set('Medium')

    button_frame = tk.Frame(add_task_window)
    button_frame.pack(pady=10)

    add_task_button = tk.Button(button_frame, text="Add Task", command=save_task)
    add_task_button.pack(side=tk.LEFT, padx=5)

    cancel_button = tk.Button(button_frame, text="Cancel", command=cancel_task)
    cancel_button.pack(side=tk.RIGHT, padx=5)

    # Bind the Enter key to the save_task function
    add_task_window.bind('<Return>', save_task)

    # Optionally, focus the title entry field to make it easier to start typing
    title_entry.focus_set()

def update_task():
    """Open a dialog to update the selected task."""
    selected_task_index = get_selected_task()
    if selected_task_index is not None:
        task = tasks[selected_task_index]

        def save_update(event=None):
            title = title_entry.get()
            description = description_entry.get()
            due_date = due_date_entry.get()
            priority = priority_combobox.get().lower()
            
            if priority not in ['low', 'medium', 'high']:
                messagebox.showerror("Error", "Priority must be 'low', 'medium', or 'high'.")
                return
            
            task.title = title
            task.description = description
            task.due_date = due_date
            task.priority = priority
            update_task_list()
            update_task_window.destroy()

        def cancel_update():
            """Close the popup without saving."""
            update_task_window.destroy()

        # Create a new window for updating the task
        update_task_window = tk.Toplevel(app)
        update_task_window.title("Update Task")
        update_task_window.geometry("300x250")

        tk.Label(update_task_window, text="Title:").pack(pady=5)
        title_entry = tk.Entry(update_task_window, width=40)
        title_entry.insert(0, task.title)
        title_entry.pack(pady=5)

        tk.Label(update_task_window, text="Description:").pack(pady=5)
        description_entry = tk.Entry(update_task_window, width=40)
        description_entry.insert(0, task.description)
        description_entry.pack(pady=5)

        tk.Label(update_task_window, text="Due Date:").pack(pady=5)
        due_date_entry = tk.Entry(update_task_window, width=40)
        due_date_entry.insert(0, task.due_date)
        due_date_entry.pack(pady=5)

        tk.Label(update_task_window, text="Priority:").pack(pady=5)
        priority_combobox = ttk.Combobox(update_task_window, values=['Low', 'Medium', 'High'])
        priority_combobox.set(task.priority.capitalize())
        priority_combobox.pack(pady=5)

        button_frame = tk.Frame(update_task_window)
        button_frame.pack(pady=10)

        update_task_button = tk.Button(button_frame, text="Update Task", command=save_update)
        update_task_button.pack(side=tk.LEFT, padx=5)

        cancel_button = tk.Button(button_frame, text="Cancel", command=cancel_update)
        cancel_button.pack(side=tk.RIGHT, padx=5)

        # Bind the Enter key to the save_update function
        update_task_window.bind('<Return>', save_update)

        # Optionally, focus the title entry field to make it easier to start typing
        title_entry.focus_set()
    else:
        messagebox.showwarning("Update Task", "Select a task to update")

def delete_task():
    selected_task = get_selected_task()
    if selected_task is not None:
        tasks.pop(selected_task)
        update_task_list()
    else:
        messagebox.showwarning("Delete Task", "Select a task to delete")

def mark_task_completed():
    selected_task = get_selected_task()
    if selected_task is not None:
        task_index = selected_task
        tasks[task_index].completed = True
        priority = tasks[task_index].priority
        if priority == 'high':
            animate_task_completion(high_listbox, task_index)
        elif priority == 'medium':
            animate_task_completion(medium_listbox, task_index)
        elif priority == 'low':
            animate_task_completion(low_listbox, task_index)
        update_task_list()
    else:
        messagebox.showwarning("Mark Completed", "Select a task to mark as completed")

def update_task_list():
    # Clear existing items
    high_listbox.delete(0, tk.END)
    medium_listbox.delete(0, tk.END)
    low_listbox.delete(0, tk.END)

    for i, task in enumerate(tasks):
        task_str = str(task)
        if task.priority == 'high':
            index = high_listbox.insert(tk.END, task_str)
            high_listbox.itemconfig(index, {'bg': get_task_color(task)})
        elif task.priority == 'medium':
            index = medium_listbox.insert(tk.END, task_str)
            medium_listbox.itemconfig(index, {'bg': get_task_color(task)})
        elif task.priority == 'low':
            index = low_listbox.insert(tk.END, task_str)
            low_listbox.itemconfig(index, {'bg': get_task_color(task)})

def get_selected_task():
    if high_listbox.curselection():
        return high_listbox.curselection()[0]
    elif medium_listbox.curselection():
        return medium_listbox.curselection()[0]
    elif low_listbox.curselection():
        return low_listbox.curselection()[0]
    else:
        return None

def save_tasks():
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(f"{task.title},{task.description},{task.due_date},{task.priority},{task.completed}\n")
    messagebox.showinfo("Save Tasks", "Tasks saved successfully")

def load_tasks():
    if os.path.exists('tasks.txt'):
        tasks.clear()  # Clear existing tasks
        with open('tasks.txt', 'r') as file:
            for line in file:
                title, description, due_date, priority, completed = line.strip().split(',', 4)
                task = Task(title, description, due_date, priority)
                task.completed = completed == 'True'
                tasks.append(task)
        update_task_list()
        messagebox.showinfo("Load Tasks", "Tasks loaded successfully")
    else:
        messagebox.showwarning("Load Tasks", "No tasks file found")

# Set up the GUI
app = tk.Tk()
app.title("To-Do List Application")
app.configure(bg='#e0f7fa')  # Set background color for the main window

frame = tk.Frame(app, bg='#e0f7fa')
frame.pack(pady=10)

# Create separate Listboxes for different priorities
high_frame = tk.Frame(frame, bg='#ff6666', padx=5, pady=5)
high_frame.pack(side=tk.LEFT, padx=10)
tk.Label(high_frame, text="High Priority", bg='#ff6666', font=('Arial', 12, 'bold')).pack()
high_listbox = tk.Listbox(high_frame, width=50, height=15, bg='#ffffff', font=('Arial', 12))
high_listbox.pack()

medium_frame = tk.Frame(frame, bg='#ffcc66', padx=5, pady=5)
medium_frame.pack(side=tk.LEFT, padx=10)
tk.Label(medium_frame, text="Medium Priority", bg='#ffcc66', font=('Arial', 12, 'bold')).pack()
medium_listbox = tk.Listbox(medium_frame, width=50, height=15, bg='#ffffff', font=('Arial', 12))
medium_listbox.pack()

low_frame = tk.Frame(frame, bg='#66ccff', padx=5, pady=5)
low_frame.pack(side=tk.LEFT, padx=10)
tk.Label(low_frame, text="Low Priority", bg='#66ccff', font=('Arial', 12, 'bold')).pack()
low_listbox = tk.Listbox(low_frame, width=50, height=15, bg='#ffffff', font=('Arial', 12))
low_listbox.pack()

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Custom button colors
button_color = '#4caf50'
button_hover_color = '#45a049'

def on_enter(e):
    e.widget.config(bg=button_hover_color)

def on_leave(e):
    e.widget.config(bg=button_color)

def on_click(e):
    e.widget.config(bg=button_hover_color)

def bind_button_to_enter(button, command):
    """Bind Enter key to the button's command."""
    def enter_pressed(event):
        command()
    button.bind('<Return>', enter_pressed)

buttons = [
    ("Add Task", add_task),
    ("Update Task", update_task),
    ("Delete Task", delete_task),
    ("Mark Completed", mark_task_completed),
    ("Save Tasks", save_tasks),
    ("Load Tasks", load_tasks)
]

button_frame = tk.Frame(app, bg='#e0f7fa')
button_frame.pack(pady=10)

for idx, (text, command) in enumerate(buttons):
    button = tk.Button(button_frame, text=text, command=command, bg=button_color, fg='white', font=('Arial', 10, 'bold'))
    button.grid(row=0, column=idx, padx=5)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    button.bind("<Button-1>", on_click)
    bind_button_to_enter(button, command)  # Bind Enter key to button command

# Load tasks at startup
load_tasks()

# Run the main application loop
app.mainloop()
