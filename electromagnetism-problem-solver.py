import tkinter as tk
from tkinter import ttk, messagebox
import math

class ElectromagnetismSolver:
    def __init__(self, master):
        self.master = master
        master.title("Electromagnetism Problem Solver")
        master.geometry("600x700")

        # Problem Types and Variables
        self.problem_types = {
            "Coulomb's Law (Electrostatic Force)": ["Force", "Charge1", "Charge2", "Distance", "Coulomb Constant"],
            "Electric Field": ["Electric Field", "Force", "Charge", "Distance"],
            "Electric Potential": ["Potential", "Work", "Charge"],
            "Capacitance": ["Capacitance", "Charge", "Voltage"],
            "Magnetic Force": ["Magnetic Force", "Charge", "Velocity", "Magnetic Field"]
        }

        # Variable Storage
        self.variables = {}

        # Setup UI
        self.create_widgets()

    def create_widgets(self):
        # Problem Type Selection
        tk.Label(self.master, text="Select Problem Type:", font=("Arial", 12)).pack(pady=10)
        self.problem_type_var = tk.StringVar()
        problem_type_dropdown = ttk.Combobox(
            self.master, 
            textvariable=self.problem_type_var, 
            values=list(self.problem_types.keys()),
            state="readonly",
            width=50
        )
        problem_type_dropdown.pack(pady=10)
        problem_type_dropdown.bind("<<ComboboxSelected>>", self.update_variables)

        # Variable Input Frame
        self.input_frame = tk.Frame(self.master)
        self.input_frame.pack(pady=20)

        # Add Variable Button
        self.add_var_button = tk.Button(
            self.master, 
            text="Add Variable", 
            command=self.add_variable_input,
            state=tk.DISABLED
        )
        self.add_var_button.pack(pady=10)

        # Solve Button
        self.solve_button = tk.Button(
            self.master, 
            text="Solve Problem", 
            command=self.solve_problem,
            state=tk.DISABLED
        )
        self.solve_button.pack(pady=10)

        # Result Display
        self.result_label = tk.Label(self.master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def update_variables(self, event=None):
        # Clear existing inputs
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        # Enable add variable and solve buttons
        self.add_var_button.config(state=tk.NORMAL)
        self.solve_button.config(state=tk.NORMAL)

        # Create first input row
        self.add_variable_input()

    def add_variable_input(self):
        # Create a new row for variable input
        row_frame = tk.Frame(self.input_frame)
        row_frame.pack(fill='x', pady=5)

        # Variable Selection Dropdown
        var_options = self.problem_types[self.problem_type_var.get()]
        var_dropdown = ttk.Combobox(
            row_frame, 
            values=var_options, 
            state="readonly", 
            width=20
        )
        var_dropdown.pack(side=tk.LEFT, padx=5)

        # Value Entry
        value_entry = tk.Entry(row_frame, width=20)
        value_entry.pack(side=tk.LEFT, padx=5)

        # Remove Button
        remove_button = tk.Button(
            row_frame, 
            text="X", 
            command=lambda: row_frame.destroy()
        )
        remove_button.pack(side=tk.LEFT, padx=5)

    def solve_problem(self):
        # Reset previous results
        self.result_label.config(text="")
        self.variables.clear()

        # Collect input variables
        for child in self.input_frame.winfo_children():
            # Find dropdown and entry widgets
            dropdown = child.winfo_children()[0]
            entry = child.winfo_children()[1]

            variable = dropdown.get()
            try:
                value = float(entry.get())
                self.variables[variable] = value
            except (ValueError, tk.TclError):
                # Skip empty or invalid entries
                continue

        # Solve based on problem type
        problem_type = self.problem_type_var.get()
        try:
            if problem_type == "Coulomb's Law (Electrostatic Force)":
                result = self.solve_coulombs_law()
            elif problem_type == "Electric Field":
                result = self.solve_electric_field()
            elif problem_type == "Electric Potential":
                result = self.solve_electric_potential()
            elif problem_type == "Capacitance":
                result = self.solve_capacitance()
            elif problem_type == "Magnetic Force":
                result = self.solve_magnetic_force()
            
            # Display result
            if result:
                self.result_label.config(text=f"Solution: {result}")
            else:
                messagebox.showinfo("Insufficient Information", "Not enough variables to solve the problem.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def solve_coulombs_law(self):
        # Coulomb's Law: F = k * (q1 * q2) / r^2
        k = 8.99e9  # Coulomb's constant
        
        # Check which variable needs to be calculated
        if "Force" not in self.variables:
            if all(var in self.variables for var in ["Charge1", "Charge2", "Distance"]):
                q1 = self.variables["Charge1"]
                q2 = self.variables["Charge2"]
                r = self.variables["Distance"]
                force = k * (q1 * q2) / (r ** 2)
                return f"{force} N"
        
        # Add more solving logic for other variable combinations
        return None

    def solve_electric_field(self):
        # Electric Field: E = F / q
        k = 8.99e9  # Coulomb's constant
        
        if "Electric Field" not in self.variables:
            if all(var in self.variables for var in ["Force", "Charge"]):
                force = self.variables["Force"]
                charge = self.variables["Charge"]
                electric_field = force / charge
                return f"{electric_field} N/C"
        
        return None

    def solve_electric_potential(self):
        # Electric Potential: V = W / q
        if "Potential" not in self.variables:
            if all(var in self.variables for var in ["Work", "Charge"]):
                work = self.variables["Work"]
                charge = self.variables["Charge"]
                potential = work / charge
                return f"{potential} V"
        
        return None

    def solve_capacitance(self):
        # Capacitance: C = Q / V
        if "Capacitance" not in self.variables:
            if all(var in self.variables for var in ["Charge", "Voltage"]):
                charge = self.variables["Charge"]
                voltage = self.variables["Voltage"]
                capacitance = charge / voltage
                return f"{capacitance} F"
        
        return None

    def solve_magnetic_force(self):
        # Magnetic Force: F = qvB
        if "Magnetic Force" not in self.variables:
            if all(var in self.variables for var in ["Charge", "Velocity", "Magnetic Field"]):
                charge = self.variables["Charge"]
                velocity = self.variables["Velocity"]
                magnetic_field = self.variables["Magnetic Field"]
                force = charge * velocity * magnetic_field
                return f"{force} N"
        
        return None

def main():
    root = tk.Tk()
    app = ElectromagnetismSolver(root)
    root.mainloop()

if __name__ == "__main__":
    main()
