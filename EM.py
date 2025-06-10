import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import math
import numpy as np


class Particle:
    def __init__(self, x, y, charge, particle_type):
        self.x = x
        self.y = y
        self.charge = charge  # in Coulombs or elementary charges
        self.particle_type = particle_type  # 'proton' or 'electron'
        self.sign = 1 if particle_type == "proton" else -1


class ElectrostaticsCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Electrostatics Calculator")
        self.root.geometry("1000x700")

        # Constants
        self.k = 8.99e9  # Coulomb's constant in N⋅m²/C²
        self.epsilon_0 = 8.854e-12  # Permittivity of free space

        # Data storage
        self.particles = []
        self.current_mode = None  # 'add_proton', 'add_electron', or None

        # GUI setup
        self.setup_main_interface()

    def setup_main_interface(self):
        # Main frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Button frame
        button_frame = tk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(0, 10))

        # Buttons
        self.add_proton_btn = tk.Button(
            button_frame,
            text="Add Positive Particle",
            command=self.toggle_proton_mode,
            bg="blue",
            fg="white",
        )
        self.add_proton_btn.pack(side=tk.LEFT, padx=5)

        self.add_electron_btn = tk.Button(
            button_frame,
            text="Add Negative Particle",
            command=self.toggle_electron_mode,
            bg="red",
            fg="white",
        )
        self.add_electron_btn.pack(side=tk.LEFT, padx=5)

        self.calculate_btn = tk.Button(
            button_frame,
            text="Calculate",
            command=self.open_calculation_window,
            bg="green",
            fg="white",
        )
        self.calculate_btn.pack(side=tk.LEFT, padx=5)

        # Clear button
        clear_btn = tk.Button(button_frame, text="Clear All", command=self.clear_all)
        clear_btn.pack(side=tk.LEFT, padx=5)

        # Canvas for cartesian plane
        self.canvas = tk.Canvas(
            main_frame, width=800, height=600, bg="white", relief=tk.SUNKEN, bd=2
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Button-1>", self.canvas_click)

        # Status label
        self.status_label = tk.Label(
            main_frame,
            text="Click 'Add Positive Particle' or 'Add Negative Particle' to start",
            relief=tk.SUNKEN,
            anchor=tk.W,
        )
        self.status_label.pack(fill=tk.X, pady=(5, 0))

        self.draw_grid()

    def draw_grid(self):
        """Draw cartesian coordinate system"""
        self.canvas.delete("grid")

        width = self.canvas.winfo_width() or 800
        height = self.canvas.winfo_height() or 600

        # Center lines (axes)
        center_x, center_y = width // 2, height // 2
        self.canvas.create_line(
            0, center_y, width, center_y, fill="black", width=2, tags="grid"
        )
        self.canvas.create_line(
            center_x, 0, center_x, height, fill="black", width=2, tags="grid"
        )

        # Grid lines
        for i in range(0, width, 40):
            self.canvas.create_line(i, 0, i, height, fill="lightgray", tags="grid")
        for i in range(0, height, 40):
            self.canvas.create_line(0, i, width, i, fill="lightgray", tags="grid")

        # Labels
        self.canvas.create_text(
            width - 20, center_y - 20, text="X", font=("Arial", 12), tags="grid"
        )
        self.canvas.create_text(
            center_x + 20, 20, text="Y", font=("Arial", 12), tags="grid"
        )
        self.canvas.create_text(
            center_x - 20, center_y + 20, text="0", font=("Arial", 10), tags="grid"
        )

    def canvas_to_coords(self, canvas_x, canvas_y):
        """Convert canvas coordinates to cartesian coordinates"""
        width = self.canvas.winfo_width() or 800
        height = self.canvas.winfo_height() or 600
        center_x, center_y = width // 2, height // 2

        x = (canvas_x - center_x) / 20  # Scale factor
        y = (center_y - canvas_y) / 20  # Inverted Y axis
        return x, y

    def coords_to_canvas(self, x, y):
        """Convert cartesian coordinates to canvas coordinates"""
        width = self.canvas.winfo_width() or 800
        height = self.canvas.winfo_height() or 600
        center_x, center_y = width // 2, height // 2

        canvas_x = center_x + x * 20
        canvas_y = center_y - y * 20
        return canvas_x, canvas_y

    def toggle_proton_mode(self):
        self.current_mode = "add_proton"
        self.status_label.config(text="Click on the plane to place a positive particle")
        self.canvas.config(cursor="crosshair")

    def toggle_electron_mode(self):
        self.current_mode = "add_electron"
        self.status_label.config(text="Click on the plane to place a negative particle")
        self.canvas.config(cursor="crosshair")

    def canvas_click(self, event):
        if self.current_mode in ["add_proton", "add_electron"]:
            x, y = self.canvas_to_coords(event.x, event.y)

            # Ask for charge
            charge = simpledialog.askfloat(
                "Charge Input",
                f"Enter charge for {self.current_mode.split('_')[1]} at ({x:.1f}, {y:.1f}):",
                initialvalue=1.0,
            )

            if charge is not None:
                particle_type = (
                    "proton" if self.current_mode == "add_proton" else "electron"
                )
                particle = Particle(x, y, abs(charge), particle_type)
                self.particles.append(particle)
                self.draw_particle(particle)

            self.current_mode = None
            self.canvas.config(cursor="")
            self.status_label.config(
                text=f"Particle added. Total particles: {len(self.particles)}"
            )

    def draw_particle(self, particle):
        canvas_x, canvas_y = self.coords_to_canvas(particle.x, particle.y)
        color = "blue" if particle.particle_type == "proton" else "red"

        # Draw particle
        self.canvas.create_oval(
            canvas_x - 8,
            canvas_y - 8,
            canvas_x + 8,
            canvas_y + 8,
            fill=color,
            outline="black",
            width=2,
        )

        # Draw charge label
        sign = "+" if particle.particle_type == "proton" else "-"
        self.canvas.create_text(
            canvas_x,
            canvas_y - 20,
            text=f"{sign}{particle.charge}",
            font=("Arial", 10, "bold"),
        )

    def clear_all(self):
        self.particles = []
        self.canvas.delete("all")
        self.draw_grid()
        self.status_label.config(text="All particles cleared")

    def open_calculation_window(self):
        if not self.particles:
            messagebox.showwarning("No Particles", "Please add some particles first!")
            return

        calc_window = tk.Toplevel(self.root)
        calc_window.title("Calculations")
        calc_window.geometry("600x500")

        # Display current particles
        particles_frame = tk.LabelFrame(
            calc_window, text="Current Particles", padx=10, pady=10
        )
        particles_frame.pack(fill=tk.X, padx=10, pady=10)

        particles_text = tk.Text(particles_frame, height=6, width=70)
        particles_text.pack()

        for i, p in enumerate(self.particles):
            sign = "+" if p.particle_type == "proton" else "-"
            particles_text.insert(
                tk.END,
                f"Particle {i+1}: {p.particle_type.capitalize()} at ({p.x:.2f}, {p.y:.2f}), Charge: {sign}{p.charge}\n",
            )
        particles_text.config(state=tk.DISABLED)

        # Calculation options
        calc_frame = tk.LabelFrame(
            calc_window, text="Select Calculation", padx=10, pady=10
        )
        calc_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        calculations = [
            ("Electric Field at a Point", self.calc_electric_field),
            ("Electric Potential at a Point", self.calc_electric_potential),
            ("Force on a Charge", self.calc_force_on_charge),
            ("Potential Energy of the System", self.calc_potential_energy),
            ("Electric Flux", self.calc_electric_flux),
            ("Gauss's Law", self.calc_gauss_law),
            ("Dipole Moment of the System", self.calc_dipole_moment),
        ]

        for text, command in calculations:
            btn = tk.Button(
                calc_frame,
                text=text,
                command=lambda cmd=command: self.perform_calculation(cmd, calc_window),
            )
            btn.pack(fill=tk.X, pady=2)

        # Navigation buttons
        nav_frame = tk.Frame(calc_window)
        nav_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Button(nav_frame, text="Back to Plane", command=calc_window.destroy).pack(
            side=tk.LEFT, padx=5
        )
        tk.Button(nav_frame, text="Close Program", command=self.root.quit).pack(
            side=tk.RIGHT, padx=5
        )

    def perform_calculation(self, calc_function, parent_window):
        try:
            result = calc_function()
            self.show_result(result, parent_window)
        except Exception as e:
            messagebox.showerror("Calculation Error", f"Error in calculation: {str(e)}")

    def show_result(self, result, parent_window):
        result_window = tk.Toplevel(parent_window)
        result_window.title("Calculation Result")
        result_window.geometry("500x400")

        # Result display
        result_frame = tk.LabelFrame(result_window, text="Result", padx=10, pady=10)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        result_text = tk.Text(result_frame, wrap=tk.WORD)
        result_text.pack(fill=tk.BOTH, expand=True)
        result_text.insert(tk.END, result)
        result_text.config(state=tk.DISABLED)

        # Navigation buttons
        nav_frame = tk.Frame(result_window)
        nav_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Button(
            nav_frame,
            text="Back to Plane",
            command=lambda: [result_window.destroy(), parent_window.destroy()],
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(
            nav_frame, text="Back to Calculations", command=result_window.destroy
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(nav_frame, text="Close Program", command=self.root.quit).pack(
            side=tk.RIGHT, padx=5
        )

    def calc_electric_field(self):
        point_x = simpledialog.askfloat("Input", "Enter X coordinate of the point:")
        point_y = simpledialog.askfloat("Input", "Enter Y coordinate of the point:")

        if point_x is None or point_y is None:
            return "Calculation cancelled."

        E_x, E_y = 0, 0

        for particle in self.particles:
            dx = point_x - particle.x
            dy = point_y - particle.y
            r = math.sqrt(dx**2 + dy**2)

            if r == 0:
                return "Error: Point coincides with a particle!"

            # Electric field magnitude
            E_mag = self.k * particle.charge * particle.sign / (r**2)

            # Components
            E_x += E_mag * (dx / r)
            E_y += E_mag * (dy / r)

        E_total = math.sqrt(E_x**2 + E_y**2)
        angle = math.degrees(math.atan2(E_y, E_x))

        return (
            f"Electric Field at ({point_x}, {point_y}):\n\n"
            f"Ex = {E_x:.2e} N/C\n"
            f"Ey = {E_y:.2e} N/C\n"
            f"Magnitude = {E_total:.2e} N/C\n"
            f"Direction = {angle:.1f}° from +x axis"
        )

    def calc_electric_potential(self):
        point_x = simpledialog.askfloat("Input", "Enter X coordinate of the point:")
        point_y = simpledialog.askfloat("Input", "Enter Y coordinate of the point:")

        if point_x is None or point_y is None:
            return "Calculation cancelled."

        V = 0

        for particle in self.particles:
            dx = point_x - particle.x
            dy = point_y - particle.y
            r = math.sqrt(dx**2 + dy**2)

            if r == 0:
                return "Error: Point coincides with a particle!"

            V += self.k * particle.charge * particle.sign / r

        return f"Electric Potential at ({point_x}, {point_y}):\n\n" f"V = {V:.2e} V"

    def calc_force_on_charge(self):
        test_charge = simpledialog.askfloat("Input", "Enter test charge (C):")
        point_x = simpledialog.askfloat("Input", "Enter X coordinate of test charge:")
        point_y = simpledialog.askfloat("Input", "Enter Y coordinate of test charge:")

        if None in [test_charge, point_x, point_y]:
            return "Calculation cancelled."

        F_x, F_y = 0, 0

        for particle in self.particles:
            dx = point_x - particle.x
            dy = point_y - particle.y
            r = math.sqrt(dx**2 + dy**2)

            if r == 0:
                return "Error: Test charge coincides with a particle!"

            # Force magnitude
            F_mag = self.k * test_charge * particle.charge * particle.sign / (r**2)

            # Components
            F_x += F_mag * (dx / r)
            F_y += F_mag * (dy / r)

        F_total = math.sqrt(F_x**2 + F_y**2)
        angle = math.degrees(math.atan2(F_y, F_x))

        return (
            f"Force on charge {test_charge} C at ({point_x}, {point_y}):\n\n"
            f"Fx = {F_x:.2e} N\n"
            f"Fy = {F_y:.2e} N\n"
            f"Magnitude = {F_total:.2e} N\n"
            f"Direction = {angle:.1f}° from +x axis"
        )

    def calc_potential_energy(self):
        if len(self.particles) < 2:
            return "Need at least 2 particles to calculate potential energy!"

        U = 0

        for i in range(len(self.particles)):
            for j in range(i + 1, len(self.particles)):
                p1, p2 = self.particles[i], self.particles[j]
                dx = p2.x - p1.x
                dy = p2.y - p1.y
                r = math.sqrt(dx**2 + dy**2)

                U += self.k * (p1.charge * p1.sign) * (p2.charge * p2.sign) / r

        return f"Potential Energy of the System:\n\n" f"U = {U:.2e} J"

    def calc_electric_flux(self):
        radius = simpledialog.askfloat("Input", "Enter radius of Gaussian surface:")
        center_x = simpledialog.askfloat("Input", "Enter X coordinate of center:")
        center_y = simpledialog.askfloat("Input", "Enter Y coordinate of center:")

        if None in [radius, center_x, center_y]:
            return "Calculation cancelled."

        enclosed_charge = 0

        for particle in self.particles:
            dx = particle.x - center_x
            dy = particle.y - center_y
            distance = math.sqrt(dx**2 + dy**2)

            if distance <= radius:
                enclosed_charge += particle.charge * particle.sign

        flux = enclosed_charge / self.epsilon_0

        return (
            f"Electric Flux through Gaussian surface:\n\n"
            f"Center: ({center_x}, {center_y})\n"
            f"Radius: {radius}\n"
            f"Enclosed charge: {enclosed_charge:.2e} C\n"
            f"Electric flux: {flux:.2e} N⋅m²/C"
        )

    def calc_gauss_law(self):
        return (
            self.calc_electric_flux() + "\n\nGauss's Law: ∮ E⋅dA = Q_enclosed/ε₀\n"
            "This calculation uses Gauss's law to find the electric flux."
        )

    def calc_dipole_moment(self):
        if len(self.particles) < 2:
            return "Need at least 2 particles to calculate dipole moment!"

        # Calculate electric dipole moment
        p_x, p_y = 0, 0
        total_charge = 0

        for particle in self.particles:
            charge = particle.charge * particle.sign
            p_x += charge * particle.x
            p_y += charge * particle.y
            total_charge += charge

        p_magnitude = math.sqrt(p_x**2 + p_y**2)

        # Find center of charge
        if total_charge != 0:
            center_note = f"Note: System has net charge of {total_charge:.2e} C"
        else:
            center_note = "System is electrically neutral"

        return (
            f"Electric Dipole Moment of the System:\n\n"
            f"px = {p_x:.2e} C⋅m\n"
            f"py = {p_y:.2e} C⋅m\n"
            f"Magnitude = {p_magnitude:.2e} C⋅m\n\n"
            f"{center_note}"
        )

    def run(self):
        # Ensure proper grid drawing after window is displayed
        self.root.after(100, self.draw_grid)
        self.root.mainloop()


if __name__ == "__main__":
    app = ElectrostaticsCalculator()
    app.run()
