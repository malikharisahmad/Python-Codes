import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        feet = int(feet_entry.get())
        inches = int(inches_entry.get())
        
        height_m = (feet * 12 + inches) * 0.0254  
        
        bmi = weight / (height_m ** 2)
        
        if bmi < 18.5:
            category = "Underweight"
            color = "blue"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            color = "green"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            color = "orange"
        else:
            category = "Obese"
            color = "red"
        
        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}", fg=color)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x400")
root.configure(bg="#f5f5f5")

header_frame = tk.Frame(root, bg="#4CAF50", pady=10)
header_frame.pack(fill="x")

header_label = tk.Label(header_frame, text="BMI Calculator", font=("Arial", 16, "bold"), fg="white", bg="#4CAF50")
header_label.pack()

main_frame = tk.Frame(root, bg="white", padx=20, pady=20)
main_frame.pack(pady=10, padx=10, fill="both", expand=True)

tk.Label(main_frame, text="Enter Weight (kg):", font=("Arial", 12), bg="white").grid(row=0, column=0, pady=5, sticky="w")
weight_entry = tk.Entry(main_frame, font=("Arial", 12))
weight_entry.grid(row=0, column=1, pady=5)

tk.Label(main_frame, text="Enter Height:", font=("Arial", 12), bg="white").grid(row=1, column=0, pady=5, sticky="w")
feet_entry = tk.Entry(main_frame, font=("Arial", 12), width=5)
feet_entry.grid(row=1, column=1, sticky="w")
tk.Label(main_frame, text="ft", font=("Arial", 12), bg="white").grid(row=1, column=1, padx=40, sticky="w")

inches_entry = tk.Entry(main_frame, font=("Arial", 12), width=5)
inches_entry.grid(row=1, column=1, padx=80, sticky="w")
tk.Label(main_frame, text="in", font=("Arial", 12), bg="white").grid(row=1, column=1, padx=120, sticky="w")

calculate_btn = tk.Button(main_frame, text="Calculate BMI", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=calculate_bmi)
calculate_btn.grid(row=2, column=0, columnspan=2, pady=15)

result_label = tk.Label(main_frame, text="", font=("Arial", 14, "bold"), bg="white")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()