import tkinter as tk
from tkinter import ttk, messagebox
from calc_function import MicroscopeCalculator


class MicroscopeCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Microscope Specimen Size Calculator")
        self.root.geometry("800x600")
        self.root.resizable(True, True)

        self.calculator = MicroscopeCalculator()

        self.create_widgets()
        self.load_specimens()

    def create_widgets(self):
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Input section
        input_frame = ttk.LabelFrame(main_frame, text="Specimen Information", padding="10")
        input_frame.pack(fill=tk.X, pady=10)

        # Specimen name
        ttk.Label(input_frame, text="Specimen Name:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.name_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.name_var, width=30).grid(row=0, column=1, sticky=tk.W, pady=5)

        # Magnified size
        ttk.Label(input_frame, text="Magnified Size (units):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.magnified_size_var = tk.DoubleVar()
        ttk.Entry(input_frame, textvariable=self.magnified_size_var, width=30).grid(row=1, column=1, sticky=tk.W,
                                                                                    pady=5)

        # Magnification factor
        ttk.Label(input_frame, text="Magnification Factor:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.magnification_factor_var = tk.DoubleVar()
        ttk.Entry(input_frame, textvariable=self.magnification_factor_var, width=30).grid(row=2, column=1, sticky=tk.W,
                                                                                          pady=5)

        # Calculate button
        ttk.Button(input_frame, text="Calculate & Save", command=self.calculate_and_save).grid(row=3, column=0,
                                                                                               columnspan=2, pady=10)

        # Results section
        result_frame = ttk.LabelFrame(main_frame, text="Calculation Result", padding="10")
        result_frame.pack(fill=tk.X, pady=10)

        ttk.Label(result_frame, text="Actual Size:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.actual_size_var = tk.StringVar(value="--")
        ttk.Label(result_frame, textvariable=self.actual_size_var, font=("Arial", 12, "bold")).grid(row=0, column=1,
                                                                                                    sticky=tk.W, pady=5)

        # Database records section
        records_frame = ttk.LabelFrame(main_frame, text="Saved Specimens", padding="10")
        records_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Create treeview for displaying records
        columns = ("ID", "Name", "Magnified Size", "Magnification", "Actual Size", "Date Added")
        self.tree = ttk.Treeview(records_frame, columns=columns, show="headings")

        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(records_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        # Pack treeview and scrollbar
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Refresh button
        ttk.Button(main_frame, text="Refresh Data", command=self.load_specimens).pack(pady=5)

    def calculate_and_save(self):
        try:
            name = self.name_var.get()
            magnified_size = self.magnified_size_var.get()
            magnification_factor = self.magnification_factor_var.get()

            if not name:
                messagebox.showerror("Error", "Please enter a specimen name")
                return

            actual_size = self.calculator.save_specimen(name, magnified_size, magnification_factor)

            # Update result display
            self.actual_size_var.set(f"{actual_size:.6f} units")

            # Refresh the specimens list
            self.load_specimens()

            # Clear input fields
            self.name_var.set("")
            self.magnified_size_var.set(0.0)
            self.magnification_factor_var.set(0.0)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def load_specimens(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Get specimens from database
        specimens = self.calculator.get_all_specimens()

        # Insert specimens into treeview
        for specimen in specimens:
            self.tree.insert("", tk.END, values=specimen)


if __name__ == "__main__":
    root = tk.Tk()
    app = MicroscopeCalculatorApp(root)
    root.mainloop()