import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

# Dictionary to store student data
students = {
    "Fredylov": {"Java": [15, 10], "Merise": [13, 00], "UML": [11, 15], "Maths": [9, 12], "ICT": [15, 2],
                  "Database": [78, 00], "SQL": [18, 19]},
    "Nolan": {"Java": [18, 12], "Merise": [10, 7], "UML": [15, 10], "Maths": [9, 8], "ICT": [10, 5],
              "Database": [2, 18], "SQL": [10, 13]},
    "Audrey": {"Java": [2, 5], "Merise": [11, 11], "UML": [10, 15], "Maths": [8, 19], "ICT": [18, 8],
               "Database": [7, 12], "SQL": [19, 11]},
    "Joel": {"Java": [12, 8], "Merise": [13, 18], "UML": [10, 11], "Maths": [5, 10], "ICT": [14, 14],
             "Database": [15, 12], "SQL": [00, 00]},
    "Ashu": {"Java": [14, 3], "Merise": [2, 8], "UML": [15, 11], "Maths": [12, 10], "ICT": [17, 14],
             "Database": [15, 14], "SQL": [12, 11]}
}

# Function to calculate the average
def calculate_average(student_name):
    student_data = students.get(student_name, {})
    if not student_data:
        return []

    averages = []
    for subject, marks in student_data.items():
        average = (marks[0] + marks[1]) / 2
        averages.append((subject, marks[0], marks[1], average))

    return averages

# Function to display student results
def display_student_result():
    student_name = student_entry.get()
    try:
        student_index = int(student_name)
        if student_index < 1 or student_index > len(students):
            raise ValueError
        student_name = list(students.keys())[student_index - 1]
    except ValueError:
        pass

    student_averages = calculate_average(student_name)

    # Clear the text widget
    result_text.delete(1.0, tk.END)

    # Display the student results in the text widget
    if not student_averages:
        student_entry.config({"foreground": "red"})
        result_text.insert(tk.END, "Student not found!")
        return

    for average in student_averages:
        result_text.insert(tk.END, f"Subject: {average[0]}\nCA: {average[1]}\nSN: {average[2]}\nRESULT: {average[3]}\n\n")

# Function to display all student names
def view_all_students():
    student_names = list(students.keys())
    result_text.delete(1.0, tk.END)
    for i, name in enumerate(student_names, start=1):
        result_text.insert(tk.END, f"{i}. {name}\n")
    result_text.insert(tk.END, "\n")

# Main Application Window
root = tk.Tk()
root.title("Student Result App")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window size based on screen resolution
window_width = int(screen_width * 0.8)
window_height = int(screen_height * 0.6)
window_position_x = (screen_width - window_width) // 2
window_position_y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{window_position_x}+{window_position_y}")
root.configure(bg='skyblue')  # Set background color

# Header Label
header_label = ttk.Label(root, text="Student Result App", font=("Arial", 24, "bold"), foreground="darkblue",
                         background="skyblue")
header_label.pack(pady=20)

# View All Results Button
view_button = ttk.Button(root, text="View All Students", command=view_all_students)
view_button.pack(pady=10)

# Input Frame
input_frame = ttk.Frame(root, padding=20)
input_frame.pack(fill=tk.BOTH, expand=True)

# Input Label and Entry
student_label = ttk.Label(input_frame, text="Enter Student Name or Index:", font=("Arial", 14))
student_label.grid(row=0, column=0, sticky="w")
student_entry = ttk.Entry(input_frame, font=("Arial", 14))
student_entry.grid(row=0, column=1, padx=10)

# Button Frame
button_frame = ttk.Frame(root, padding=20)
button_frame.pack(fill=tk.BOTH, expand=True)

# Result Button
result_button = ttk.Button(button_frame, text="Get Student Results", command=display_student_result)
result_button.pack(side="left", padx=5)

# Result Text Frame
result_text_frame = ttk.Frame(root, padding=20)
result_text_frame.pack(fill=tk.BOTH, expand=True)

# Result Text
result_text = ScrolledText(result_text_frame, width=60, height=10, wrap=tk.WORD, font=("Arial", 12))
result_text.pack(fill=tk.BOTH, expand=True)

root.mainloop()
